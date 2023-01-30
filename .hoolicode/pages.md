
```yml
%% by url %%

api (api/):
	- products-cart-toggle/:pk (products-cart-toggle)
	- posts-comment-delete/:pk (posts-comment-delete)

lamasoft (/):
	- / (home)
	- about/ (about)
	- contact/ (contact)
	- faq/ (faq)

products (/):
	- product-list/ (product-list)
	- product/:slug (product-detail)
	- order-create/:pk (order-create)
	- review-create/:pk (review-create)
	- review-list/:pk (review-list)

users (/):
	- login/
	- register/
	- account-settings/ (account-settings)
	- account-settings-password/ (account-settings-password)
	- account-orders/ (account-order-list)
	- account-orders/:pk (account-order-detail)

posts (blog/):
	- / (post-list)
	- :year/:month/:day/:slug/ (post-detail)
vacancies (career/):
	- / (vacancy-list)
	- /:pk (vacancy-detail)
	- apply/:pk (vacancy-application-create)

forum (forum/):
	- / (question-list)
	- question-create/ (question-create)
	- :year/:month/:day/:slug (question-detail)

```

total: `25`