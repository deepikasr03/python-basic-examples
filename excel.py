def convert_excel_to_dict(excel_table):
    # Create a dictionary containing common_examples, intent_examples and entity_examples
    train_data = {u'rasa_nlu_data':{u'common_examples':[]}}
    train_data[u'rasa_nlu_data'][u'intent_examples'] = []
    train_data[u'rasa_nlu_data'][u'entity_examples'] = []
    for _, row in excel_table.iterrows():
        sample = {}
        question = str(row[QUESTION])
        if isinstance(row[INTENT], unicode) and isinstance(row[ENTITY], unicode):
            ## Both intent and 'entityName' present in csv files
            sample[u'intent'] = unicode(row[INTENT])
            sample[u'entities'] = get_entities(question, row[ENTITY])
            sample[u'text'] = unicode(''.join(re.split(r'[\[\]\{\}\(\)]+', question)))
            train_data[u'rasa_nlu_data'][u'common_examples'].append(sample)
        elif isinstance(row[INTENT], unicode) and '(' in question:
            ## Only intent present but entity marked for 'smallTalk'
            sample[u'intent'] = unicode(row[INTENT])
            sample[u'entities'] = get_entities(question, '')
            sample[u'text'] = unicode(''.join(re.split(r'[\[\]\{\}\(\)]+', question)))
            train_data[u'rasa_nlu_data']['common_examples'].append(sample)
        elif isinstance(row[INTENT], unicode) and '{' in question:
            ## Only intent present but entity marked for 'lens_type'
            sample[u'intent'] = unicode(row[INTENT])
            sample[u'entities'] = get_entities(question, '')
            sample[u'entities'][u'value'] = sample[u'entities'][u'value'].lower()
            sample[u'text'] = unicode(''.join(re.split(r'[\[\]\{\}\(\)]+', question)))
            train_data[u'rasa_nlu_data'][u'common_examples'].append(sample)
        elif isinstance(row[INTENT], unicode):
            ## Only intent present and entity not marked.
            sample[u'intent'] = unicode(row[INTENT])
            sample[u'text'] = unicode(''.join(re.split(r'[\[\]\{\}\(\)]+', question)))
            train_data[u'rasa_nlu_data'][u'intent_examples'].append(sample)
        elif not isinstance(row[INTENT], unicode):
            ## No intent only entity present
            sample[u'entities'] = get_entities(question, row[ENTITY])
            sample[u'text'] = unicode(''.join(re.split(r'[\[\]\{\}\(\)]+', question)))
            train_data[u'rasa_nlu_data'][u'entity_examples'].append(sample)
    return train_data