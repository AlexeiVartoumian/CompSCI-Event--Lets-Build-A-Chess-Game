import argparse
import collections
import configparser
from datetime import datetime
import grp , pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib

argparser = argparse.ArguemntParser(description = "silly content tracker")

argsubparsers = argparser.add_subparsers(title = "Commands", dest = "command")
argsubparsers.required = True

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add"  :   cmd_add(args)
        case "cat-file" :   cmd_cat_file(args)
        case "check-ignore" :cmd_check_ignore(args)
        case "checkout" : cmd_checkout(args)
        case "commit" : cmd_commit(args)
        case "hash-object" : cmd_has_object(args)
        case "init" : cmd_init(args)
        case "log" : cmd_log(args)
        case "ls-files" : cmd_ls_files(args)
        case "ls-tree" : cmd_ls_tree(args)
        case "rev-parse" : cmd_rev_parse(args)
        case "rm" : cmd_rm(args)
        case "show-ref" : cmd_show_ref(args)
        case "status" : cmd_status(args)
        case "tag" : cmd_tag(args)
        case _ : print("bad command")

class GitRepository(object):
    "git repo"
    worktree = None
    gitdir = None
    conf = None

    def __init__(self , path , force= False):
        self.worktree = path
        self.gitdir = os.path.join(path , ".git")

        if not ( force or os.path.isdir(self.gitdir) ):
            raise Exception("Not a git repository %s" % path)
        
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")
        
        if not force:
            version= int(self.conf.get("core" , "repositoryformatversion"))

            if version != 0:
                raise Exception("Unsupported repositoryformatversion %s " % version)
    
    def repo_path(repo , *path):
        "calculate path "
        return os.path.join(repi.getdir , *path)
    
    def repo_file(repo , *path, mkdir= False):
        "like repo path but create dirnaim id not ther"
        if repo_dir(repo, *path[:-1],mkdir=mkdir)
            return repo_path(repo, *path)
    

    def repo_dir(repo , *path , mkdir= False):

        path = repo_path(repo, *path)

        if os.path.exists(path):
            if (os.path.isdir(path)):
                return path
            else:
                raise Exception("not a directory %s" % path)

        if mkdir:
            os.makedirs(path)
            return path
        else:
            return None
    
    def repo_create(path):
        "create new pore at path"

        repo = Gitrepository(path , True)

        if os.path.exists(repo.worktree):
            raise Exception(" %s is not a directory" % path)
        if os.path.exists(repo.getdir) and os.listdir(repi.gitdir)
            raise Exception("%s is not empty!" % path)
        else:
            os.makedirs(repo.worktree)
        
        assert repo_dir(repo, "brnaches" , mkdir= True)
        assert repo_dir(repo, "objects" , mkdir = True)
        assert repo_dir(repo, "refs", "tags", mkdir= True)
        assert repo_dir(repo, "refs", "heads", mkdir = True)

        with open(repo_file(repo , "description"), "w") as f:
            f.write("unamed repositu edit hits file  'description' to name the repository ")
        
        with open(repo_file(repo , "HEAD"), "w") as f:
            f.write("ref: refs/heads/master\n")
        
        with open(repo_file(repo , "config"), "w") as f :
            config = repo_default_config()
            config.write(f)
        
        return repo

    #create ini file with configparser library
    def repo_default_config():
        ret = configparser.ConfigParser()
        ret.add_section("core")
        ret.set("core", "repositoryformatversion", "0")
        ret.set("core" , "filemode", "false")
        ret.set("core", "bare" , "false")
    
        return ret

    argsp = argsubparsers.add_parser("init" , help ="initialise an ewn empty repositou" )   
    argsp.add_argument("path",
    metavar = "directory,
    nargs = "?",
    default = ".",
    help = "where to create repository")


    def cmd_init(args):
        # C:\Users\alexv\OneDrive\Documents\Ctest\wyag.sh init test
        repo_create(args.path)
    
    def repo_find(path = "." , required = True):
        path = os.path.realpath(path)

        if os.path.isdir(os.path.join(path, ".git")):
            return GitRepository(path)
        
        parent = os.path.realpath(os.path.join(path, ".."))

        if parent == path:

            if required:
                raise Exception ("no git directory")
            else:
                return None
            
        return repo_find(parent , required)
    

class GitObject(object):

    def __init__(self , data = None):
        
        if data != None:
            self.deserialize(data)
        else:
            self.init()
    
    # two i=unimplmented methods sub class will imple 
    def serilaize( self , repo):
        """this function must be implemente by sublcasses
        it will read objects contents from self.data , a byte string ad ndo wahatever it takes to conver it into meaningful representation depending on subc lass
        """
        raise Exception("Unimplemented")
    
    def deserialize(self, data): 
        raise Exception("Unimplemented")
    
    def init(self):
        pass

    def object_read(repo , sha):

        path = repo_file(repo , "objects", sha[0:2], sha[2:])

        if not os.path.isfile(path):
            return None
        
        with open(path , "rb") as f:
            raw = zlib.decompress(f.read())

            #read obj type
            x = raw.find(b' ')
            fmt = raw[0:x]

            #read and validate obbject size
            y = raw.find(b'\x00', x)
            size = int(raw[x:y].decode("ascii"))
            if size != len(raw)-y-1:
                raise Exception("Malformed obect{0}: bad length".format(sha))
            
            match fmt:

                case b'commit' : c= GitCommit
                case b'tree' : c = GitTree
                case b'tag' : c=GitTag
                case b'blob' : c = GitBlob
                case _ :
                    raise Exception("Unknown type {0} for object{1}".format(fmt.decode("ascii"),sha))
                
            return c(raw[y+1:])
    
    def object_write(obj , repo=None):
        #seruliase ibject data
        data = obj.serialize()

        result = obj.fmt + b' ' + str(len(data)).encode() + b'\x00' + data

        sha = hashlib.sha1(result).hexdigest()

        if repo:
            path = repo_file(repo , "objects", sha[0:2], sha[2:],mkdir = True)

            if not os.path.exists(path):
                with open(path , 'wb') as f:
                    f.write(zlib.compress(result))
        return sha


class GitBlob(GitObject):
    fmt = b'blob'

    def serialize(self):
        return self.blobdata
    
    def deserialize(self,data):
        self.blobdata = data

    argsp = argsubparsers.add_parser("cat-file" , 
    help = "provide content of repository objects")

    argsp.add_argument("type", metavar = "type",
    choices = ["blob", "commit", "tag" , "tree"],
    help = "specify the type")

    argsp.add_argument("object", metvar = "object", help = "the object to display")

    def cmd_cat_file(args):
        repo = repo_find()
        cat_file(repo,args.object, fmt=args.type.encode())

    def cat_file(repo, obj, fmt = None):
        obj = object_read(repo, object_find(repo, obj , fmt=fmt))
        sys.stdout.buffer.write(obj.serialize())

    def object_find(repo, name , fmt=None , follow = True):
        return name # temp placeholder
    

    argsp = argsubparsers.add_parser("hash-object", help = "Compute object id and optionally creates a blob from a file")

    argsp.add_argument("-t",
    metavar = "type",
    dest = "type",
    choices = ["blob", "commit", "tag" , "tree"],
    default = "blob"
    help = "specify the type" )

    argsp.add_argument("-w",
    dest= "write",
    action = "store_true",
    help = "acutally write the object into the database")

    argsp.add_argument("path", help = "read object from <file>")

    def cmd_hash_object(args):
        if args.write:
            repo = repo_find()
        else:
            repo = None
        
        with open(args.path , "rb") as fd:
            sha = object_hash(fd , args.type.encode(), repo)
            print(sha)
    
    def object_hash(fs, fmt, repo = None):
        "Hash obkect writing it to repo if provided"
        data = fd.read()

        match fmt:
            case b'commit' : obj= GitCommit(data)
            case b'tree': obj = GitTree(data)
            case b'tag': obj = GitTag(data)
            case b'blob' : obj = GitBlob(data)
            case _ : raise Exception("Unknown type %s" % fmt)

        return object_write(obj ,repo)






