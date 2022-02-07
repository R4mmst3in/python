import pandas as pd


df = pd.read_csv('survey_results_public.csv')
df_schema = pd.read_csv('survey_results_schema.csv')

    print(df)
    print(df.shape)
    print(df.shape)
    print(df.shape)
    print(df.shape)
    print(df.shape)
    print(df.info())
    pd.set_option('display.max_columns',85)


print(df_schema)
print(df_schema.head(10))
print(df_schema.tail(20))

# print(df_schema.shape)
print(df.columns)
print(df['Employment'])
print(df['Employment'].value_counts())
