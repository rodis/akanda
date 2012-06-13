import errno

from PF import PacketFilter, PFAddr, PFPort, PFRule, PFRuleAddr, PFRuleset

from akanda import exceptions


def pf_factory():
    pf = PacketFilter()
    try:
        pf.enable()
    except IOError, (err, msg):
        if err == errno.EACCES:
            raise exceptions.PermissionDenied()
        elif err == errno.ENOTTY:
            raise exceptions.UnsupportedIOCTL()
        elif err == errno.EOPNOTSUPP:
            raise exceptions.OperationNotSupported()
        elif err == errno.ENODEV:
            raise exceptions.OperationNotSupportedByDevice()
    return pf


def print_states(pf):
    states = pf.get_states() or []
    if not states:
        print "No state information."
        return
    for state in states:
        nk, sk = state.nk, state.sk
        s = "{0}".format(state.nk.addr[1])
        if nk.port[1]:
                s += (":{0}" if state.af == AF_INET else "[{0}]").format(nk.port[1])
        if (nk.addr[1] != sk.addr[1] or nk.port[1] != sk.port[1]):
            s += " ({0}".format(sk.addr[1])
            if sk.port[1]:
                s += (":{0})" if state.af == AF_INET else "[{0}])").format(sk.port[1])
        s += (" -> " if state.direction == PF_OUT else " <- ")
        s += "{0}".format(nk.addr[0])
        if nk.port[0]:
            s += (":{0}" if state.af == AF_INET else "[{0}]").format(nk.port[0])
        if (nk.addr[0] != sk.addr[0] or nk.port[0] != sk.port[0]):
            s += " ({0}".format(sk.addr[0])
            if sk.port[0]:
                s += (":{0})" if state.af == AF_INET else "[{0}])").format(sk.port[0])
        print "State {0.id:#x} on {0.ifname} ({1})".format(state, s)
        print "   Packets: {0.packets[0]}:{0.packets[1]}".format(state)
        print "   Bytes: {0.bytes[0]}:{0.bytes[1]}".format(state)
        print "   Expires in {0.expire} seconds".format(state)


def get_rules():
    r1 = PFRule()
    r2 = PFRule()
    rs = PFRuleset()
    rs.append(r1, r2)
    return rs

def block_in_pass_out()
    
