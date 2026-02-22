import pandas as pd 

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score



# dataset
def load_data( filename ):

    try:

        data=pd.read_csv( filename )

        return data

    except FileNotFoundError:

        print( "Error: CSV file not found" )

        return None




# explore data
def explore_data( data ):
    
    print( "\nBasic Statistics:" )

    print( data.describe() )



# visualize data
def plot_data( data ):

    plt.scatter( data["Size"], data["Price"] )

    plt.ylabel( "House Price ($)" )

    plt.title( "House Size vs Price" )

    plt.show()


# linear regression 
def train_model( data ):

    X = data[["Size"]]  

    y = data["Price"]  

    model = LinearRegression()

    model.fit(X, y)


    predictions = model.predict(X)

    print( "\nModel Results:" )

    print( f"Coefficient (Slope): {model.coef_[0]:.2f}" )

    print( f"Intercept: {model.intercept_:.2f}" )

    print( f"R² Score: {r2_score(y, predictions):.3f}" )

    return model


def plot_regression( data, model ):

    plt.scatter( data["Size"], data["Price"] )

    plt.plot( data["Size"], model.predict( data[["Size"]] ) )

    plt.xlabel( "House Size (sqft)" )

    plt.ylabel( "House Price ($)" )

    plt.title( "Linear Regression Model Fit" )

    plt.show()


# predict price with user-input
def predict_price( model ):

    while True:

        try:

            size = float(input( "\nEnter house size in sqft (or -1 to exit): " ))

            if size == -1:

                break

            if size <= 0:

                print( "Size must be a positive number." )

                continue


            price = model.predict([[size]])

            print( f"Estimated House Price: ${price[0]:,.2f}" )

        except ValueError:

            print( "Invalid input. Please enter a numeric value." )



# main
def main():

    print( "Housing Price Prediction Using Linear Regression" )

    data = load_data( "housing_data.csv" )

    if data is None:

        return

    explore_data( data )

    plot_data( data )

    model = train_model( data )

    plot_regression( data, model )

    predict_price( model )

    print( "\nProgram finished." )


if __name__ == "__main__":
    main()