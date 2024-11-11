import pandas as pd

df = pd.read_csv("../data/2024/clean_data/survey_data.csv")

print(df)

answered_contribute_docs_question = df.dropna(subset="LIKERT.CONTRIBUTOR_TYPE.CONTRIBUTE_DOCS")

print(answered_contribute_docs_question["LIKERT.CONTRIBUTOR_TYPE.CONTRIBUTE_DOCS"].value_counts(normalize=True))
