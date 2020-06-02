import os
import pandas as pd
path = './lagouCompany.csv'
if not os.path.exists('./lagouJobs.csv'):
    col_names = ['companyUrl', 'companyName', 'companyRealName', 'companyHireNumber', 'CVprocessingRate',
                 'CVprocessingDay', 'commentNumebr', 'lastLoginDate', 'companyScale', 'companyLocation',
                 'companyIntroduce', 'companyDeveloping']
    df = pd.DataFrame(columns=col_names)
    df.to_csv(path_or_buf=path, encoding='GB18030', index=False)
