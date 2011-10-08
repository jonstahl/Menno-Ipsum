from nltk import parse_cfg, ChartParser
from random import choice

def produce(grammar, symbol):
    words = []
    productions = grammar.productions(lhs = symbol)
    production = choice(productions)
    for sym in production.rhs():
        if isinstance(sym, str):
            words.append(sym)
        else:
            words.extend(produce(grammar, sym))
    return words

grammar = parse_cfg('''
S_full -> S | SubConj S ',' S
S -> NP VP
PP -> P NP_no_PP | 'to get more billable hours' | 'in our wheelhouse' | 'in the bullpen' | 'in the cloud' | 'in the wiki' | 'in the wild' | 'in the streets' | 'with conviction'
NP -> Det N | Det AP N | Det N PP | N_plural | AP N_plural | AP N_plural PP | N_proper
NP_no_PP -> Det N | Det AP N | N_plural | AP N_plural | N_proper
VP -> Vtrans NP | Vintrans | VP PP
Vintrans -> 'iterates' | 'adds value' | 'innovates' | 'sucks less' | 'is connected' 
Vtrans -> 'leverages' | 'creates' | 'pings' | 'postmortems' | 'refactors' | 'dogfoods' | 'asymptotically approaches' | 'engages' | 'networks with' | 'organizes' 
AP -> AP | A
Det -> 'a' | 'the' | 'every'
Det_plural -> 'some' | 'all' | 'most'
A -> 'suboptimal' | 'tactical' | 'global' | 'nontrivial' | 'scrummy' | 'granular' | 'batshit crazy' | 'nonprofit' | 'open source' | 'performant' | 'hybrid' 
N_plural -> 'trees' | 'analytics' | 'metrics' | 'best practices' | 'strategies' | 'engagement superpowers' | 'API limits' | 'funders' | 'audiences' | 'supporters' | 'members'
N_proper -> 'I' | 'Gideon Rosenblatt' | 'Wilco' | 'Little House on the Prairie' | 'Groundwire' | 'Neal Myrick' | 'Plone' | 'Salesforce' | 'Skype' | 'Rally' | 'an agile process' | 'a bunch of technobabbling punks' | 'grooming the backlog' | 'the environmental movement' | 'the full meal deal' | 'what good looks like' | 'HQ' | 'Jon Stahl' | 'Groundwire Labs'
N -> 'synergy' | 'bandwidth' | 'theory of change' | 'sprint' | 'wordle' | 'bucket' | 'campaign' | 'low-hanging fruit' | 'sprint planning' | 'technology' | 'user story' | 'engagement' | 'movement as network' | 'social change' | 'data migration' | 'innovation' | 'capacity building' | 'theming' | 'advanced functionality' | 'Engagement Pyramid' | 'Gantt chart' | 'scope' | 'scrumbucket' | 'consulting' | 'engagement level' | 'utilization rate' | 'Chipotle order' | 'penguin' | 'line of sight' | 'situational awareness'
P -> 'in' | 'outside' | 'to' | 'on' | 'about' | 'around'
SubConj -> 'although' | 'because' | 'while' | 'after' | 'as' | 'before' | 'if' | 'as long as' | 'since' | 'though' | 'unless' | 'whenever'
''')

parser = ChartParser(grammar)
gr = parser.grammar()

def build_sentence():
    words = produce(gr, gr.start())
    sentence = ' '.join(words).replace(' ,', ',') + '.'
    sentence = sentence[0].upper() + sentence[1:]
    return sentence

if __name__ == '__main__':
    for i in range(10):
        print build_sentence()
