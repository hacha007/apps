import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   

# App title
st.title("Hachem's DATA ANALYSER")

# Upload CSV data
uploaded_files = st.file_uploader("Upload your input CSV files", type=["csv"], accept_multiple_files=True)
if uploaded_files:
    dataframes = {uploaded_file.name: pd.read_csv(uploaded_file) for uploaded_file in uploaded_files}
    selected_file = st.selectbox("Select a dataset", list(dataframes.keys()))
    st.write(dataframes[selected_file].head())

    if selected_file:
        st.write("Dataset Description:")
        st.write(dataframes[selected_file].describe())

        # Select a variable from the dataset
        variable = st.selectbox("Select a variable", dataframes[selected_file].columns)

        # Determine the type of the selected variable
        if pd.api.types.is_numeric_dtype(dataframes[selected_file][variable]):
            graph_type = st.selectbox("Select a graph type", ["Histogram", "Boxplot", "Scatterplot"])
        else:
            graph_type = st.selectbox("Select a graph type", ["Barplot", "Countplot"])

        # Draw the selected graph
        if graph_type == "Histogram":
            st.write("Histogram")
            fig, ax = plt.subplots()
            ax.hist(dataframes[selected_file][variable], bins=30)
            st.pyplot(fig)
        elif graph_type == "Boxplot":
            st.write("Boxplot")
            fig, ax = plt.subplots()
            sns.boxplot(y=dataframes[selected_file][variable], ax=ax)
            st.pyplot(fig)
        elif graph_type == "Scatterplot":
            st.write("Scatterplot")
            other_variable = st.selectbox("Select another variable for scatter plot", dataframes[selected_file].columns)
            fig, ax = plt.subplots()
            ax.scatter(dataframes[selected_file][variable], dataframes[selected_file][other_variable])
            st.pyplot(fig)
        elif graph_type == "Barplot":
            st.write("Barplot")
            fig, ax = plt.subplots()
            sns.barplot(x=dataframes[selected_file][variable].value_counts().index, y=dataframes[selected_file][variable].value_counts().values, ax=ax)
            st.pyplot(fig)
        elif graph_type == "Countplot":
            st.write("Countplot")
            fig, ax = plt.subplots()
            sns.countplot(x=dataframes[selected_file][variable], ax=ax)
            st.pyplot(fig)
