from nltk import CFG, ChartParser
from random import choice
import re

def produce(grammar, symbol):
    words = []
    productions = grammar.productions(lhs = symbol)
    production = choice(productions)
    for sym in production.rhs():
        if isinstance(sym, unicode):
            words.append(sym)
        else:
            words.extend(produce(grammar, sym))
    return words

grammar = CFG.fromstring('''
S_full -> S | SubConj S ',' S
S -> NP VP | NP_plural VP_plural
PP -> P NP | P_phrase
PP_adverbial -> P_adverbial NP | P_phrase | 'to get more billable hours' | 'with conviction'
P_phrase -> 'in our wheelhouse' | 'in the bullpen' | 'in the cloud' | 'in the wiki' | 'in the wild' | 'in the streets'
NP        -> Det N | Det AP N | Det N PP | N_proper | N_collective | Det_plural N_collective | AP N_collective | Det_plural AP N_collective | N_collective PP | Det_plural N_collective PP
NP_plural -> Det_plural N_plural | Det_plural AP N_plural | N_plural | AP N_plural | NP_plural PP
VP        -> Vtrans NP | Vintrans | 'is' A | VP PP_adverbial
VP_plural -> Vtrans_plural NP | Vintrans_plural | 'are' A | VP_plural PP_adverbial
Vintrans        -> 'iterates' | 'adds value' | 'innovates' | 'sucks less' | 'is connected' 
Vintrans_plural -> 'iterate'  | 'add value'  | 'innovate'  | 'suck less'  | 'are connected'
Vtrans        -> 'leverages' | 'creates' | 'pings' | 'postmortems' | 'refactors' | 'dogfoods' | 'asymptotically approaches' | 'engages' | 'networks with' | 'organizes'
Vtrans_plural -> 'leverage'  | 'create'  | 'ping'  | 'postmortem'  | 'refactor'  | 'dogfood'  | 'asymptotically approach'   | 'engage'  | 'network with'  | 'organize'
AP -> AP | A
Det -> 'a' | 'the' | 'every'
Det_plural -> 'the' | 'some' | 'all' | 'most'
A -> 'suboptimal' | 'tactical' | 'global' | 'nontrivial' | 'scrummy' | 'granular' | 'batshit crazy' | 'nonprofit' | 'open source' | 'performant' | 'hybrid' 
N_plural -> 'trees' | 'metrics' | 'best practices' | 'strategies' | 'engagement superpowers' | 'API limits' | 'funders' | 'audiences' | 'supporters' | 'members' | 'concentric circles'
N_proper -> 'Gideon Rosenblatt' | 'Wilco' | 'Little House on the Prairie' | 'Groundwire' | 'Neal Myrick' | 'Plone' | 'Salesforce' | 'Skype' | 'Rally' | 'an agile process' | 'a bunch of technobabbling punks' | 'grooming the backlog' | 'the environmental movement' | 'the full meal deal' | 'what good looks like' | 'HQ' | 'Jon Stahl' | 'Groundwire Labs' | 'GWBase'
N -> 'theory of change' | 'sprint' | 'wordle' | 'bucket' | 'campaign' | 'user story' | 'Engagement Pyramid' | 'Gantt chart' | 'scope' | 'scrumbucket' | 'engagement level' | 'utilization rate' | 'Chipotle order' | 'penguin' | 'line of sight'
N_collective -> 'analytics' | 'synergy' | 'bandwidth' | 'low-hanging fruit' | 'sprint planning' | 'technology' | 'engagement' | 'movement as network' | 'social change' | 'data migration' | 'innovation' | 'capacity building' | 'theming' | 'advanced functionality' | 'consulting' | 'situational awareness' | 'change management'
P -> 'in' | 'outside' | 'on' | 'about' | 'around' | 'of'
P_adverbial -> 'in' | 'outside' | 'on' | 'about' | 'around' | 'less than' | 'more than'
SubConj -> 'although' | 'because' | 'while' | 'after' | 'as' | 'before' | 'if' | 'as long as' | 'since' | 'though' | 'unless' | 'whenever'
''')

parser = ChartParser(grammar)
gr = parser.grammar()

A_RE = re.compile(r'\ba ([aeiou])', re.IGNORECASE)

def build_sentence():
    words = produce(gr, gr.start())
    sentence = ' '.join(words).replace(' ,', ',') + '.'
    sentence = A_RE.sub(r'an \1', sentence)
    sentence = sentence[0].upper() + sentence[1:]
    return sentence

if __name__ == '__main__':
    print build_sentence()
