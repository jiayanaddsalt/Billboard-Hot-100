from statsmodels.formula.api import ols
import statsmodels.api as sm

def ols_summary_plot(y, x, df):
    '''
    Analyzes the shift of musics features from 1950 to 2015
    Inputs:
        y: string, the name of dependent variable
        x: string, the name of independent variable
        df: pandas dataframe, data source of the analysis
    Outputs:
        OLS Regression Results and a scatter plot with a linear regression line
    '''

    mod = ols(formula='{} ~ {}'.format(y, x), data = df).fit()
    print(mod.summary())
    ax = df.groupby(x, as_index=False) \
                .mean() \
                .plot(x=x, y=y, kind='scatter',
                    title='Shift of {} with the increase of {}'.format(y, x), grid=True);

    fig = sm.graphics.abline_plot(model_results=mod, ax=ax)
