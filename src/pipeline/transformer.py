def transform_data(preprocessor, X):
    """
    Applies the fitted preprocessing pipeline to the input features.

    Args:
        preprocessor: ColumnTransformer or Pipeline
        X (pd.DataFrame): Input features

    Returns:
        np.array or sparse matrix: Transformed features
    """
    return preprocessor.fit_transform(X)
