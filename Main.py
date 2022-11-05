import reviewProcess
import pandas

# customer list
cus_list_air = []
cus_list_pro = []

# review list
review_list_air = []
review_list_pro = []

# rating list
star_list_air = []
star_list_pro = []

# data list
date_list_air = []
date_list_pro = []

# Update the review pages of macbook air
x = 1
while x > 0:
    soup_air = reviewProcess.getSoup(f'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/product-reviews/B08N5KWB9H/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}&sortBy=recent')
    reviewProcess.find_customer(soup_air, cus_list_air)
    reviewProcess.find_review(soup_air, review_list_air)
    reviewProcess.find_rating(soup_air, star_list_air)
    reviewProcess.find_date(soup_air, date_list_air)

    print("ac" + str(len(cus_list_air)))
    print("ar" + str(len(review_list_air)))
    print("as" + str(len(star_list_air)))
    print("ad" + str(len(date_list_air)))

    if not soup_air.find('li', {'class': 'a-disabled a-last'}):
        x = x + 1
    else:
        break


# Update the review pages of macbook pro
y = 1
while y > 0:
    soup_pro = reviewProcess.getSoup(f'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/product-reviews/B08N5N6RSS/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber={y}&sortBy=recent')
    reviewProcess.find_customer(soup_pro, cus_list_pro)
    reviewProcess.find_review(soup_pro, review_list_pro)
    reviewProcess.find_rating(soup_pro, star_list_pro)
    reviewProcess.find_date(soup_pro, date_list_pro)

    print("pc" + str(len(cus_list_pro)))
    print("pr" + str(len(review_list_pro)))
    print("ps" + str(len(star_list_pro)))
    print("pd" + str(len(date_list_pro)))

    if not soup_pro.find('li', {'class': 'a-disabled a-last'}):
        y = y + 1
    else:
        break


# divide the dataset into two parts, positive and negative
cus_positive_air, cus_negative_air, review_positive_air, review_negative_air, star_positive_air, star_negative_air, \
 date_positive_air, date_negative_air \
 = reviewProcess.divide_review(cus_list_air, review_list_air, star_list_air, date_list_air)

cus_positive_pro, cus_negative_pro, review_positive_pro, review_negative_pro, star_positive_pro, star_negative_pro, \
 date_positive_pro, date_negative_pro \
 = reviewProcess.divide_review(cus_list_pro, review_list_pro, star_list_pro, date_list_pro)

# create the dataset for data frame
data_air = {'Name': cus_list_air, 'Review': review_list_air, 'Rating': star_list_air, 'Date': date_list_air}
data_pro = {'Name': cus_list_pro, 'Review': review_list_pro, 'Rating': star_list_pro, 'Date': date_list_pro}

data_air_positive = {'Name': cus_positive_air, 'Review': review_positive_air, 'Rating': star_positive_air, 'Date': date_positive_air}
data_air_negative = {'Name': cus_negative_air, 'Review': review_negative_air, 'Rating': star_negative_air, 'Date': date_negative_air}

data_pro_positive = {'Name': cus_positive_pro, 'Review': review_positive_pro, 'Rating': star_positive_pro, 'Date': date_positive_pro}
data_pro_negative = {'Name': cus_negative_pro, 'Review': review_negative_pro, 'Rating': star_negative_pro, 'Date': date_negative_pro}

# create data frames
df_air = pandas.DataFrame(data_air)
df_pro = pandas.DataFrame(data_pro)

df_air_positive = pandas.DataFrame(data_air_positive)
df_air_negative = pandas.DataFrame(data_air_negative)

df_pro_positive = pandas.DataFrame(data_pro_positive)
df_pro_negative = pandas.DataFrame(data_pro_negative)

print(star_list_pro)

df_air.to_csv('/Users/yuyu/macbook_air_reviews.csv')
df_pro.to_csv('/Users/yuyu/macbook_pro_reviews.csv')
df_air_positive.to_csv('/Users/yuyu/macbook_air_reviews_positive.csv')
df_air_negative.to_csv('/Users/yuyu/macbook_air_reviews_negative.csv')
df_pro_positive.to_csv('/Users/yuyu/macbook_pro_reviews_positive.csv')
df_pro_negative.to_csv('/Users/yuyu/macbook_pro_reviews_negative.csv')


