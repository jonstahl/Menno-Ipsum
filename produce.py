from nltk import CFG, ChartParser
from random import choice
import re


def produce(grammar, symbol):
    words = []
    productions = grammar.productions(lhs=symbol)
    try:
        production = choice(productions)
    except Exception as e:
        raise Exception(f"Error with production {symbol}")
    for sym in production.rhs():
        if isinstance(sym, str):
            words.append(sym)
        else:
            words.extend(produce(grammar, sym))
    return words


grammar = CFG.fromstring(
    """
S_full -> S | SubConj S ',' S
S -> NP VP | NP_plural VP_plural
PP -> P NP
P_phrase -> 'of tomorrow'
PP_adverbial -> P_adverbial NP | P_phrase
NP        -> Det N | Det AP N | Det N PP | N_proper | N_collective | Det_plural N_collective | AP N_collective | Det_plural AP N_collective | N_collective PP | Det_plural N_collective PP
NP_plural -> Det_plural N_plural | Det_plural AP N_plural | N_plural | AP N_plural | NP_plural PP
VP        -> Vtrans NP | Vintrans | 'is' A | VP PP_adverbial
VP_plural -> Vtrans_plural NP | Vintrans_plural | 'are' A | VP_plural PP_adverbial
Vintrans        -> 'drives customer success' | 'innovates' | 'drinks the champagne'
Vintrans_plural -> 'drive customer success'  | 'innovate'  | 'drink the champagne'
Vtrans        -> 'unlocks' | 'extends' | 'creates' | 'loops in' | 'pings' | 'architects' | 'accelerates'
Vtrans_plural -> 'unlock'  | 'extend'  | 'create'  | 'loop in ' | 'ping'  | 'architect'  | 'accelerate'
AP -> AP | A
Det -> 'a' | 'the' | 'every'
Det_plural -> 'the' | 'some' | 'all' | 'most'
A -> 'global' | 'best-practice' | 'open source' | 'agile' | 'Lightning' | 'Einstein' | 'cloud-based' | 'Summer' | 'Winter' | 'Spring'
N_plural -> 'trees' | 'metrics' | 'best practices' | 'governor limits'
N_proper -> 'Marc Benioff' | 'Salesforce.org' | 'Quip' | 'Tableau' | 'Work.com' | 'Salesforce' | 'Zoom' | 'the 4th industrial revolution' | 'Customer 360' | 'the platform' | 'Ohana' | 'Astro' | 'Codey' | 'Appy' | 'SaaSy' | 'Cloudy' | 'Einstein' | 'the 1-1-1 model' | 'Dreamforce' | 'Apex' | 'the AppExchange' | 'Chatter' | 'the Metadata API' | 'the Tooling API' | 'Trailhead' | 'the Hub' | 'the Open Source Commons' | '"clicks not code"'
N -> 'community sprint' | 'account' | 'contact' | 'campaign' | 'opportunity' | 'user story' | 'bug' | 'release' | 'org' | 'instance' | 'partner' | 'ISV' | 'customer' | 'Trailblazer'
N_collective -> 'analytics' | 'sprint planning' | 'backlog grooming' | 'technology' | 'digital experience' | 'social change' | 'data migration' | 'innovation' | 'business' | 'trust' | 'customer success' | 'equality'
P -> 'in' | 'outside' | 'on' | 'about' | 'around' | 'of'
P_adverbial -> 'in' | 'outside' | 'on' | 'about' | 'around' | 'less than' | 'more than'
SubConj -> 'although' | 'because' | 'while' | 'after' | 'as' | 'before' | 'if' | 'as long as' | 'since' | 'though' | 'unless' | 'whenever'
"""
)

parser = ChartParser(grammar)
gr = parser.grammar()

A_RE = re.compile(r"\ba ([aeiou])", re.IGNORECASE)


def build_sentence():
    words = produce(gr, gr.start())
    sentence = " ".join(words).replace(" ,", ",") + "."
    sentence = A_RE.sub(r"an \1", sentence)
    sentence = sentence[0].upper() + sentence[1:]
    return sentence


if __name__ == "__main__":
    print(build_sentence())
