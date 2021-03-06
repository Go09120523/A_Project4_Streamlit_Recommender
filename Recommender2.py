# Import packages---------------------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pickle
# import warnings
# warnings.filterwarnings('ignore')

# st.set_page_config(layout="wide")
# pd.options.display.float_format = '{:.2f}'.format
# st.set_option('deprecation.showPyplotGlobalUse', False)

# Input files----------------------------------------------------------------------
products = pd.read_csv('Product_new.csv')
reviews = pd.read_csv('Review_new.zip', lineterminator='\n')
with open('Sim_Results.pkl', 'rb') as f:
    prod_rec = pickle.load(f)
user_rec = pd.read_parquet('user_recs.parquet')  #

st.write('hello')

# # Functions-----------------------------------------------------------------------------
# reviews[['customer_id', 'product_id', 'rating']] = reviews[['customer_id', 'product_id', 'rating']].apply(pd.to_numeric)
# # Random products for initial display
# init_display = products.sample(16, replace=False)[['item_id', 'name', 'description', 'price', 'url', 'image']]

# # Search product category in 'name'
# def search(str):
#     search = [products[products['name']==x] for x in products['name'] if str in x]
#     res = pd.concat(search)

#     return res.sample(12, replace=False)
# # Get product information
# def item(id):
#   return products.loc[products['item_id']==id]
# # Display recommendations
# def display_group (lst = init_display):
#     with st.container():
#         col1, col2, col3, col4 = st.columns(4)
#         with col1:
#             with st.container():               
#                 st.image(lst['image'].tolist()[0])
#                 st.write(lst['name'].tolist()[0][:50])
#                 st.write("Price:      " + str(lst['price'].tolist()[0]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[0]))
#             with st.container():
#                 st.image(lst['image'].tolist()[1])
#                 st.write(lst['name'].tolist()[1][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[1]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[1]))
#             with st.container():
#                 st.image(lst['image'].tolist()[2])
#                 st.write(lst['name'].tolist()[2][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[2]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[2]))
#         with col2:
#             with st.container():
#                 st.image(lst['image'].tolist()[3])
#                 st.write(lst['name'].tolist()[3][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[3]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[3]))
#             with st.container():
#                 st.image(lst['image'].tolist()[4])
#                 st.write(lst['name'].tolist()[4][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[4]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[4]))
#             with st.container():
#                 st.image(lst['image'].tolist()[5])
#                 st.write(lst['name'].tolist()[5][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[5]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[5]))
#         with col3:
#             with st.container():
#                 st.image(lst['image'].tolist()[6])
#                 st.write(lst['name'].tolist()[6][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[6]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[6]))
#             with st.container():
#                 st.image(lst['image'].tolist()[7])
#                 st.write(lst['name'].tolist()[7][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[7]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[7]))
#             with st.container():
#                 st.image(lst['image'].tolist()[8])
#                 st.write(lst['name'].tolist()[8][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[8]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[8]))
#         with col4:
#             with st.container():
#                 st.image(lst['image'].tolist()[9])
#                 st.write(lst['name'].tolist()[9][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[9]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[9]))
#             with st.container():
#                 st.image(lst['image'].tolist()[10])
#                 st.write(lst['name'].tolist()[10][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[10]))
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[10]))
#             with st.container():
#                 st.image(lst['image'].tolist()[11])
#                 st.write(lst['name'].tolist()[11][:50])
#                 st.write("Price:   " + str(lst['price'].tolist()[11])) 
#                 st.write("Product ID: " + str(lst['item_id'].tolist()[11]))  
# # Recommended products
# def recommend(item_id, num):
#     recs = prod_rec[item_id][:num]
#     lst = []
#     for rec in recs:
#         lst.append(int(rec[1]))
#     return lst

# CODE to build models is here.  Un-comment to run-----------------------------------------
# # BuildCosine-Similarity
# products = products[products['name'].notnull()]
# products['name_description'] = products.name + products.description
# products = products[products['name_description'].notnull()]
# products['name_description_pre'] = products['name_description'].apply(lambda x: word_tokenize(x, format='text'))
# products = products.reset_index()
# # stop words
# STOP_WORD_FILE = 'vietnamese-stopwords.txt'
# with open(STOP_WORD_FILE, 'r', encoding='utf-8') as file:
#   stop_words = file.read()
# stop_words = stop_words.split('\n')
# # TF-IDF
# tf = TfidfVectorizer(analyzer='word', min_df=0, stop_words=stop_words)
# tfidf_matrix = tf.fit_transform(products.name_description_pre)
# cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
# prod_rec = {}
# for idx, row in products.iterrows():
#     similar_indices = cosine_similarities[idx].argsort()[:-10:-1]
#     similar_items = [(cosine_similarities[idx][i], products['item_id'][i]) for i in similar_indices]
#     prod_rec[row['item_id']] = similar_items[1:]
    
# # Build ALS Model
# reviews = spark.read.csv('data/Review_new.csv', inferSchema=True, header=True)
# reviews = reviews.withColumn('customer_id', reviews['customer_id'].cast(IntegerType()))
# reviews = reviews.withColumn('product_id', reviews['product_id'].cast(IntegerType()))
# reviews = reviews.withColumn('rating', reviews['rating'].cast(DoubleType()))
# reviews = reviews.na.drop(subset=['customer_id', 'product_id', 'rating'], how = 'any')
# reviews_sub = reviews.select('customer_id', 'product_id', 'rating')
# (training, test) = reviews_sub.randomSplit([0.8, 0.2])
# # Buil an (default) estimator
# ALS_Explicit = ALS( implicitPrefs=False, userCol='customer_id', itemCol='product_id', ratingCol="rating", coldStartStrategy="drop", nonnegative=True)
# defaultModel = ALS_Explicit.fit(training)
# # An evaluator
# evaluatorR = RegressionEvaluator(metricName="rmse", labelCol="rating")
# # Parameter map
# paramMap = ParamGridBuilder() \
#           .addGrid(ALS_Explicit.rank, [ 15,  22, 30]) \
#           .addGrid(ALS_Explicit.maxIter, [12,  20]) \
#           .addGrid(ALS_Explicit.regParam, [0.5, 0.1, 0.05]) \
#           .addGrid(ALS_Explicit.alpha, [2.0]) \
#           .build()
# # Run CrosValidation to find best model..
# CV_ALS_Explicit = CrossValidator(estimator=ALS_Explicit,
#                             estimatorParamMaps=paramMap,
#                             evaluator=evaluatorR,
#                             numFolds=3)
# CV_Model = CV_ALS_Explicit.fit(training)
# # Make predictions on test. CV_Model uses the best model found.
# model = CV_Model.bestModel
# predictions = model.transform(test)
# predictions.show(5)
# # Evaluate the model by computing the RMSE on the test data
# evaluator = RegressionEvaluator(metricName='rmse',
#                                 labelCol='rating',
#                                 predictionCol='prediction')
# rmse = evaluator.evaluate(predictions)

# # GUI---------------------------------------------------------------------

# st.title("Data Science Recommender System Project")
# st.write("---------------------------------------------------------------------------")
# st.write("Upload file contains products information used for content-base filtering")
# uploaded_file = st.file_uploader('Choose a file', type=['csv'], key=1)
# if uploaded_file is not None:
#     products2 = pd.read_csv(uploaded_file, encoding='latin-1')
#     products2.to_csv('Product_new2.csv', index=False)
# st.write("Upload file contains users information used for collaborative filtering")
# uploaded_file2 = st.file_uploader('Choose a file', type=['csv'], key=2)
# if uploaded_file2 is not None:
#     reviews2 = pd.read_csv(uploaded_file, encoding='latin-1')
#     reviews2.to_csv('Review_new2.csv', index=False)
# st.write('****************************************************************') 
# menu = ['Business Objective', 'Build Project', 'Recommender']
# choice = st.sidebar.selectbox('Menu', menu)
# if choice == 'Business Objective':
#     st.write(""" 
# - Tiki l?? m???t h??? sinh th??i th????ng m???i ???all in one???, trong ???? c?? tiki.vn, l?? m???t website th????ng m???i ??i???n t??? ?????ng top 2 c???a Vi???t Nam, top 6 khu v???c ????ng Nam ??.
# - Tr??n trang n??y ???? tri???n khai nhi???u ti???n ??ch h??? tr??? n??ng cao tr???i nghi???m ng?????i d??ng v?? h??? mu???n x??y d???ng nhi???u ti???n ??ch h??n n???a.
# """)
#     st.markdown("##### **OBJECTIVE:**")
#     st.write("X??y d???ng Recommendation System cho m???t ho???c m???t s??? nh??m h??ng \
#         ho?? tr??n tiki.vn gi??p ????? xu???t v?? g???i ?? cho kh??ch h??ng trong qu?? tr??nh l???a ch???n s???n ph???m ")
#     st.markdown("##### **????? XU???T:**")
#     st.write("""
# - Content-base filtering algorithms such as Cosine-Similarity or Gensim for new customer product search.
# - Collaborative filtering such as ALS or DBSCAN for our regular customers""")
#     st.write("In this project, we will employ Cosine-Similarity and ALS to build Tiki Recommender System")

# elif choice == 'Build Project':
#     st.subheader('Build Project')
#     st.markdown('#### 1. Some data')
#     st.write('Product')
#     st.dataframe(products.head(3))
#     st.write('Review')
#     st.dataframe(reviews.head(3))
#     st.markdown('#### 2. Visualization')
#     st.write('Gi?? b??n')
#     fig, ax = plt.subplots(1, 2, figsize=(12,6))
#     products.price.plot(kind='box', ax=ax[0])
#     products.price.plot(kind='hist', bins=20, ax=ax[1])
#     st.pyplot(fig.figure) 
#     st.write('Th????ng hi???u')
#     brands = products.groupby('brand')['item_id'].count().sort_values(ascending=False)
#     fig = brands[1:11].plot(kind='bar')
#     plt.ylabel('Count')
#     plt.title('Products Items by brand')
#     st.pyplot(fig.figure)
#     st.write('Gi?? b??n theo th????ng hi???u')
#     price_by_brand = products.groupby(by='brand').mean()['price'].sort_values(ascending=False)
#     fig = price_by_brand[:10].plot(kind='bar')
#     plt.ylabel('Price')
#     plt.title('Average price by brand')
#     st.pyplot(fig.figure)
#     st.write('Rating')
#     fig= plt.figure(figsize=(6, 6))
#     sns.displot(products, x = 'rating', kind='hist')
#     st.pyplot(fig.figure)
#     st.write('Average Rating')
#     avg_rating_customer = reviews.groupby(by='product_id').mean()['rating'].to_frame().reset_index()
#     avg_rating_customer.rename({'rating': 'avg_rating'}, axis=1, inplace=True)
#     n_products = products.merge(avg_rating_customer, left_on='item_id', right_on = 'product_id', how='left')
#     fig= plt.figure(figsize=(6, 6))
#     sns.displot(n_products, x='avg_rating', kind='hist')
#     st.pyplot(fig.figure)
#     st.write('Review distribution')
#     fig= plt.figure(figsize=(6, 6))
#     sns.displot(reviews, x='rating', kind='kde')
#     st.pyplot(fig.figure)
#     st.write('Top 20 products have the most reviews')
#     fig = plt.figure(figsize = (12, 6))
#     top_products = reviews.groupby('product_id').count()['customer_id'].sort_values(ascending=False)[:20]
#     top_products.index = products[products.item_id.isin(top_products.index)]['name'].str[:25]
#     top_products.plot(kind='bar')
#     st.pyplot(fig.figure)
#     st.write('Top 20 customers do the most reviews')
#     top_rating_customers = reviews.groupby('customer_id').count()['product_id'].sort_values(ascending=False)[:20]
#     plt.figure(figsize=(12,6))
#     plt.bar(x=[str(x) for x in top_rating_customers.index], height=top_rating_customers.values)
#     plt.xticks(rotation=70)
#     st.pyplot(fig.figure)
#     st.markdown('#### 3. Build Model')
#     st.markdown('##### Cosine-Similarity')
#     st.markdown(""" Steps taken:
#     -  'underthesea word_tokenize' used to tokenize texts
#     -  TfidfVectorizer to number words, eliminate words in vietnamese-stopwords
#     -  cosine_similarity to get the matrix of similarity
#     -  Based on cosine-similariry matrix, for each product, we can get a certain number of similar products   
#              """)
#     st.write('The final file, which contains similar products for all products, was built and imported for later \
#         building Recommender System')
#     st.markdown('##### ALS Model')
#     st.write("Due to too much time it takes to tune the model to get the best parameter settings, the model was built \
#     in advance.  The recommendation file for all customers was also built and imported.")
#     st.write("Combination of Cosine-Similarity and ALS model is used to make product recommendation depending on users are new or old customers.")
#     st.markdown('#### 4. Model Evaluation')
#     st.write("""
#     -  Cosine-Similarity has no method to evaluate the result since it was built based on the similarity among products
#     -  The performance of the result can only be judged in real world when it is put in use""")
#     st.write('RMSE of the ALS model is ~ 1.05')
#     st.write('This model is good enough to build a Recommender System for customers in database')
# elif choice == 'Recommender':
#     st.markdown("# Hello! Welcome to Tiki Online Electronics")
#     st.markdown("###### *** Please clear/reset field before going to the next field - Sorry for the inconvinience***")
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         customer_id = st.text_input('Customer ID (6177374, 1827148...)')             
#     with col2:
#         product_id = st.text_input('Product ID (3792857, 1060082...)')            
#     with col3:
#         option = st.selectbox(
#                         'Product Keywords: ',
#                         ('Tivi', 'Loa', 'Camera', 'Laptop', 'T??? l???nh', 'Kh??c...'),
#                         index = 5)
#     if customer_id == product_id:
#         if option == 'Kh??c...' :
#             st.markdown("##### ***Suggested Products: *** ")
#             display_group()
#     if customer_id:
#         st.markdown("##### ***Suggested Products: *** ")
#         result = user_rec[user_rec['customer_id'] == int(customer_id)]
#         rec = [x['product_id'] for x in result.explode('recommendations')['recommendations']]
#         cid_display = pd.concat([products[products['item_id'] == x] for x in rec])
#         cid_display = cid_display[['item_id', 'name', 'description', 'price', 'url', 'image']]
#         display_group(cid_display)   
#     if product_id:
#         st.write("Your product: ")
#         item = item(int(product_id))
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.image(item['image'].values[0])
#         with col2:
#             with st.container():
#                 st.write(item['name'].values[0])
#                 st.write("Price:  " + str(item['price'].values[0]))
#                 st.write("Product ID:  " + str(item['item_id'].values[0]))
#         with col3:
#             st.write(item['description'].values[0][:400])
            
#         st.markdown("##### ***Similar Products: *** ")
        
#         lst = recommend(int(product_id), 10) + [73314682, 48273751]
#         cid_display = pd.concat([products[products['item_id'] == x] for x in lst])
#         cid_display = cid_display[['item_id', 'name', 'description', 'price', 'url', 'image']]
#         display_group(cid_display)
       
#     if option != 'Kh??c...':
#         display_group(search(option))
        
        
        
        
        
         
        
    