# vim: sw=4:ts=4:et:ai:hls
import os, sys, subprocess

# Helper taken from an adafuit LCD tutorial.
def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output

if __name__ == "__main__":
    # set count of differences high
    distance_from_head = 0 
    new_low = 900
    low_distance = 0
    path = "c:\\users\\joshua\\src"
    i3v = "%s\\notebook\\i3v\\Marlin_RAMPS_EPCOS_i3v\\Configuration.h"%path
    marlin = "%s\\Marlin\\Marlin\\Configuration.h"%path
    while True:
        try:
            #run_cmd("cd %s\\Marlin && git revert -n 1.0.x~%d"%(path, distance_from_head))
            run_cmd("cd %s\\Marlin && git checkout 1.0.x~%d"%(path, distance_from_head))
            #print run_cmd("cd %s\\Marlin && git status"%path)    
            #print "diff -w %s %s"%(i3v, marlin)
            output = run_cmd("diff -w %s %s"%(i3v, marlin))
            diffs = len(output.split("\n"))
            print "%d: %d"%(distance_from_head, diffs)
            if diffs < new_low:
                new_low = diffs; low_distance = distance_from_head
            distance_from_head += 1
            #run_cmd("cd %s\\Marlin && git clean -df && git checkout -- ."%path)
        except:
            break
    #print run_cmd("cd %s\\Marlin && git stash save")
    #print run_cmd("cd %s\\Marlin && git stash drop")
    #run_cmd("cd %s\\Marlin && git status"%path)    
    #run_cmd("cd %s\\Marlin && git revert --abort"%path)
    #run_cmd("cd %s\\Marlin && git checkout -- ."%path)
    #run_cmd("cd %s\\Marlin && git clean -df && git checkout -- ."%path)
    #print run_cmd("cd %s\\Marlin && git status"%path)    
    # start at HEAD
    # get count of line differences
    # go back a revision
    print "Low was at %d with %d lines different."%(low_distance, new_low)

