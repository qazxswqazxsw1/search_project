import random
from .indexer import index
from .query import Query


def score(clean_query, document):
    # Возвращает скор для пары запрос-документ
    # больше -- релевантнее
    return random.random()


def retrieve(query):
    # Возвращает начальный список релевантных документов
    # (желательно, не бесконечный)

    candidates = []
    print(query)
    print(index.get_all(query))
    for doc in index.get_all(query):
        candidates.append(index.documents[doc])
    return candidates[:50]


def score_documents(query, documents):
    # Возвращает отсортированный по релевантности массив документов и их скор
    return sorted([{'doc': doc, 'score': -score(query, doc)} for doc in documents],
                  key=lambda pair: pair['score'])


def prepare_serp(query, scored_docs):
    result = []
    for doc_score in scored_docs:
        info = doc_score['doc'].format(query)
        result.append([info['title'], info['text'], doc_score['score']])
    return result