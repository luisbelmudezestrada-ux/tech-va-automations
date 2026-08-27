import pandas as pd

# Tech VA Automation - Real Estate Lead Cleaner
# Saves 3h per list for US Realtors

def clean_leads(file_path):
    df = pd.read_csv(file_path)
    df.drop_duplicates(subset=['email'], inplace=True)
    df = df[df['phone'].str.len() > 9]
    df['city'] = df['city'].str.title().str.strip()
    df.to_csv('cleaned_leads.csv', index=False)
    print(f"Done! {len(df)} clean leads saved")
    return df
