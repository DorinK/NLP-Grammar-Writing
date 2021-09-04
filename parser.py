"""Usage: parser.py [GRAMMAR_FILE_NAME]

Arguments:
    GRAMMAR_FILE_NAME the path to the grammar file
"""
import nltk

from generate import PCFG
from nltk import PCFG as nltk_pcfg
from nltk.parse import ViterbiParser

expected_sentences = [
    #### GRAMMARICAL Part 2
    # "the sandwich ate Sally .",
    # "Sally sighed .",
    # "the president thought that Sally sighed .",
    # "it perplexed the president that a sandwich ate Sally .",
    # "it perplexed the president that Sally sighed .",
    # "it perplexed the president that it perplexed Sally that the sandwich sighed .",    # TODO: can't generate    V
    # "the president thought that a very perplexed sandwich ate a sandwich .",
    # "Sally and the president wanted and ate a sandwich .",
    # "the president thought that a sandwich sighed .",
    # "it perplexed the president that a sandwich ate Sally .",
    # "the president thought that Sally is a sandwich .",
    # "the president worked on every proposal on the desk .",
    # "Sally is eating a sandwich .",


    #### UN-GRAMMARICAL Part 2
    # "Sally and the president wanted and thought a sandwich .",
    # "Sally is perplexed a sandwich .",
    # "the president perplexed .",
    # "Sally is thought .",
    # "Sally is perplexed the president .",
    # "Sally sighed a president .",
    # "Sally sighed a sandwich .",
    # "the president thought that the president perplexed .",
    # "a very president understood .",
    # "is it true that the proposal worked the proposal ?",
    # "the president thought that the president perplexed .",
    # "Sally is perplexed the president .",
    # "Sally eating worked the chief of staff .",
    # "Sally and the president wanted and thought a sandwich .", #TODO: should support? "Sally and the president wanted and thought *on* a sandwich ." "Sally and the president thought and wanted  a sandwich ."
    # "the Sally is perplexed .",
    # "the Sally perplexed the president .",
    # "president is perplexed .",
    # "desk is perplexed .",
    # "chief of staff kissed the desk .",

    #### UN-GRAMMARICAL Part 4
    # "Sally is very .",
    # "is it true that Sally is very ?",
    # "Sally and the president perplexed ."

    #### UN-GRAMMARICAL Piazza, assighnment and Eran
    # "the very fine very fine president sighed .",
    # "the president thought that a sandwich sighed a pickle .",
    # "sally with the pickle ate a sandwich .",

    #### GRAMMARICAL Piazza, assighnment
    # "the president thought that a sandwich sighed .",
    # "The president with the pickle ate a sandwich .",

    #### Part 2 sentences
    # "sally ate a sandwich .",
    # "sally and the president wanted and ate a sandwich .",
    # "the president sighed .",
    # "the president thought that a sandwich sighed .",
    # "it perplexed the president that a sandwich ate sally .",
    # "the very very very perplexed president ate a sandwich .",
    # "the president worked on every proposal on the desk .",
    # "sally is lazy .",
    # "sally is eating a sandwich .",
    # "the president thought that sally is a sandwich .",

    # ## Part 2 as questions:
    # "did sally eat a sandwich ?",
    # "will sally eat a sandwich ?",
    # "did sally and the president want and eat a sandwich ?",
    # "will sally and the president want and eat a sandwich ?",
    # "did the president sigh ?",
    # "will the president sigh ?",
    # "did the president think that a sandwich sighed ?",
    # "will the president think that a sandwich sighed ?",
    # "did it perplex the president that a sandwich ate sally ?",
    # "will it perplex the president that a sandwich ate sally ?",
    # "did the very very very perplexed president eat a sandwich ?",
    # "will the very very very perplexed president eat a sandwich ?",
    # "did the president work on every proposal on the desk ?",
    # "will the president work on every proposal on the desk ?",
    # "is Sally lazy ?",
    # "is sally eating a sandwich ?",
    # "did the president think that sally is a sandwich ?",
    # "will the president think that sally is a sandwich ?",

    ### GRAMMARICAL Part 4 (b)
    # "will the president eat ?",
    # "did Sally eat a sandwich ?",
    # "will Sally eat a sandwich ?",
    # "will Sally eat a very perplexed sandwich ?",

    # "what did the president think ?",
    # "what did the president think that Sally ate ?",
    # "what did Sally eat the sandwich with ?",
    # "who ate the sandwich ?",
    # "where did Sally eat the sandwich ?",

    ## should pass according to git
    # "did Sally eat a sandwich ?",
    # "will Sally and the president want and eat a sandwich ?",
    # "did the president sigh ?",
    # "did the president think that a sandwich sighed ?",
    # "will a sandwich eat Sally ?",
    # "is a sandwich eating Sally ?",
    # "did it perplex the president that a sandwich ate Sally ?",
    # "did the very very very perplexed president eat a sandwich ?",
    # "is the very very very perplexed president eating a sandwich ?",
    # # "is the president working on every proposal on the desk ?",
    # "is Sally lazy ?",
    # "is Sally eating a sandwich ?",
    # "did the president think that Sally is a sandwich ?",
    # "is Sally a sandwich ?",
    # "did Sally work on a desk ?",
    # "did a president understand a pickled president ?",
    # "did a proposal work on the desk ?",
    # "is a desk the president ?",
    # "is Sally every chief of staff ?",
    # # "is a sandwich an apple ?",
    # # "is an apple a sandwich ?",
    # # "does an apple sigh ?"

    ### shouldn't pass according to git
    # "did Sally lazy ?",
    # "is very very very perplexed president eating a sandwich ?",
    # "is a desk president ?",
    # "did a proposal work on work on the desk ?",
    # "did a proposal work on sighed ?",
    # "did a proposal work on the desk on the desk ?",
    # # "does a apple sigh ?"

    # "is it true that the very pickled pickle pickled sally that every very very lazy perplexed proposal wanted that every very very very very delicious pickle wanted that the very fine chief of staff is eating a very fine pickle ?",
    #
    # "the perplexed pickled president under every pickled pickled pickled floor pickled the sandwich !",
    # "is it true that the pickled pickle pickled a delicious pickle ?",
    # "the president ate every sandwich .",
    # "a delicious pickled pickle understood the pickle .",
    # "the sandwich under a chief of staff understood every chief of staff .",
    # "is it true that every chief of staff pickled every fine perplexed pickle ?",
    # "is it true that a delicious pickle kissed every floor ?",
    # "is it true that every delicious perplexed sandwich wanted the fine perplexed president ?",
    # "every pickled floor ate every delicious fine pickled perplexed perplexed pickled delicious fine pickle .",
    # "is it true that a perplexed fine delicious president kissed a delicious floor ?"

    # "every very very delicious sandwich on a floor is fine ."
    # "what did a pickle perplex sally ?"

    # "is it true that it perplexed the very very perplexed president under a president that sally and a delicious floor and sally is pickled ?"

    # # gen part 1
    # "every fine president with every chief of staff with the floor understood every chief of staff .",
    # "the fine fine pickled president understood a delicious delicious fine sandwich !",
    # "every pickle kissed a delicious perplexed sandwich .",
    # "is it true that a president wanted every delicious sandwich ?",
    # "is it true that every fine pickle understood a pickled president ?",
    # "is it true that a delicious delicious sandwich ate every floor ?",
    # "every fine fine president ate every delicious fine delicious president !",
    # "the fine fine delicious president understood every sandwich .",
    # "every delicious fine pickle wanted a sandwich !",
    # "a delicious perplexed fine delicious floor wanted a fine delicious perplexed chief of staff !",
    #
    # # gen part 2
    # "it perplexed chandler that the chief of staff played with phoebe !",
    # "rachel ate monica .",
    # "is it true that the doctor is pickled and a perplexed chief of staff is cynical ?",
    # "the cynical perplexed doctor is a pizza !",
    # "chandler thought that it perplexed rachel that the pizza understood that rachel is ross !",
    # "ross kissed the very fine chief of staff !",
    # "joey understood that it perplexed the very very cynical doctor that it perplexed rachel that it perplexed rachel that ross sighed !",
    # "it perplexed phoebe that a chief of staff hugged a pickle .",
    # "is it true that the pizza thought that it perplexed rachel that phoebe laughed ?",
    # "chandler is kissing a doctor !",
    # "a pizza is very delicious !",
    # "is it true that the doctor is monica ?",
    # "chandler and the sandwich kissed rachel !",
    # "is it true that ross is a loyal doctor and a proposal is perplexed and very lazy ?",
    # "joey is lazy and very loyal !",
    # "is it true that ross is very funny ?",
    # "chandler is very cynical and very fine !",
    # "it perplexed joey that ross kissed a pickle and the desk worked with phoebe !",
    # "ross is eating joey and rachel !",
    # "sally is cynical and phoebe thought that rachel hugged the doctor !",
    # "sally thought that it perplexed rachel that joey smiled !",
    # "rachel is kissing monica .",
    # "chandler thought that phoebe laughed !",
    # "it perplexed monica and the sandwich that sally understood that chandler wanted monica !",
    # "joey hugged the sandwich ."
]

expected_sentences = [x.lower() for x in expected_sentences]


def grammar_to_nltk_format(grammar):
    grammar_rules_nltk_format = []
    for key, values_outter in grammar._rules.items():
        for values_inner in values_outter:
            values_inner_str = values_inner[0]
            for i, value_inner_str in enumerate(values_inner_str):
                if value_inner_str.lower() == value_inner_str:
                    values_inner_str[i] = f"'{value_inner_str}'"
            weight = values_inner[1]
            prob = weight / grammar._sums[key]
            grammar_rules_nltk_format.append(f"{key} -> {' '.join(values_inner_str)} [{prob}]")

    model = nltk_pcfg.fromstring("\n".join(grammar_rules_nltk_format))
    parser = ViterbiParser(model)

    return parser


def test_sent(sent, parser):
    result = parser.parse(sent.split(" "))
    result = set(tree.freeze() for tree in result)

    print()
    print(f"sent `{sent}` found {len(result)} tree:")
    if len(result) > 0:
        print(str(list(result)[0]))


if __name__ == '__main__':

    from docopt import docopt

    arguments = docopt(__doc__)

    pcfg = PCFG.from_file(arguments['GRAMMAR_FILE_NAME'])

    nltk_parser = grammar_to_nltk_format(pcfg)

    for sent in expected_sentences:
        test_sent(sent, nltk_parser)

    # random_sent = pcfg.random_sent(1)
    # counter = 0
    # while len(expected_sentences) > 0:
    #     counter += 1
    #     random_sent = pcfg.random_sent(1)
    #     if random_sent in expected_sentences:
    #         print(f"found sent `{random_sent}`")
    #         expected_sentences.remove(random_sent)
    #     if counter % 100000 == 0:
    #         print(counter)

    print("done")
