import akanda.pf


def run_all():
    pf = akanda.pf_factory()
    akanda.pf.print_states(pf)
    pf.load_ruleset(akanda.pf.get_rules())
    print pf.get_ruleset()
    akanda.pf.get_states(pf)
