from pyFG import FortiOS
import sys

if __name__ == '__main__':
    f = open('fortios_intf.txt', 'r')
    candidate = f.read()
    f.close()

    d = FortiOS('fortigate', username="admin", password="fortigate")#, vdom='test_vdom')

    #d = FortiOS(hostname, vdom='vpn')
    d.open()
    d.load_config('system interface', empty_candidate=True)
    d.load_config(config_text=candidate, in_candidate=True)
#    d.close()

    print "This is the diff of the conigs:"
#    for line in d.compare_config(text=True):
#        print line

    print "\n\n"
    print "This is how to reach the desired state:"
    config_changes = d.compare_config()
    print config_changes
    d.commit(config_changes)
    d.close()
