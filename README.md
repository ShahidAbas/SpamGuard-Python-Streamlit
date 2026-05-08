# SpamGuard-Python-Streamlit
SpamGuard Classifier is an NLP and Machine Learning-based application designed to detect spam and legitimate (ham) messages with high accuracy. The project uses various Natural Language Processing (NLP) techniques such as text cleaning, stopword removal, stemming with PorterStemmer, and feature extraction using CountVectorizer and TF-IDF Vectorizer.

The project was developed using Python libraries including NLTK, NumPy, Pandas, Matplotlib, Seaborn, WordCloud, and PIL for preprocessing, data analysis, and visualization. LabelEncoder was used for label transformation, while multiple machine learning models were trained and evaluated, including GaussianNB, MultinomialNB, BernoulliNB, XGBClassifier, GradientBoostingClassifier, RandomForestClassifier, ExtraTreesClassifier, DecisionTreeClassifier, and others.

Among all tested models, Multinomial Naive Bayes (MNB) achieved the best performance with a precision score of 1.0 and an accuracy above 97%, making it the most reliable model for spam detection in this project.

The final trained model was saved in .pkl format and deployed through a Streamlit-based web interface for real-time spam message prediction.

If you found this project helpful, please consider giving it a ⭐ to show your support!
