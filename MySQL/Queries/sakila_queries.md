
# MySQL Practice Queries


### ===== QUERY 1 ===== ###  
**Goal:**  Get all customers inside city_id = 312, returning customer's first name, 
last name, email, and address.  
  
**SELECT** customer.first_name, customer.last_name, customer.email, customer.address_id, costumer_list.address, city.city_id, address.address  
**FROM** customer  
**JOIN** address  
**ON** customer.address_id = address.address_id  
**WHERE** address.city_id = 312;


### ====== QUERY 2 ===== ###  
**Goal:**  Get all comedy films, returning the film title, description, release year, rating, special features, and genre (category)  
  
**SELECT** film_category.film_id, category.name, film.title, film.description, film.release_year, film.rating, film.special_features  
**FROM** film_category  
**JOIN** category  
**ON** film_category.category_id = category.category_id  
**JOIN** film  
**ON** film_category.film_id = film.film_id  
**WHERE** film_category.category_id = 5;


### ===== QUERY 3 ===== ###
**Goal:**  Get all films joined by actor_id=5, returning the actor id, 
actor name, film title, description, and release year.  
  
**SELECT** actor.actor_id, actor.first_name, actor.last_name, film.film_id, film.title, film.description, film.release_year  
**FROM** film_actor  
**JOIN** actor  
**ON** film_actor.actor_id = actor.actor_id  
**JOIN** film  
**ON** film_actor.film_id = film.film_id  
**WHERE** film_actor.actor_id = 5;


### ===== QUERY 4 ===== ###
Goal:  Get all the customers in store_id = 1 and inside the cities (1, 42, 312, 459),
return customer first name, last name, email, and address.  
  
**SELECT** address.city_id, customer.first_name, customer.last_name, customer.email, address.address, customer.store_id
**FROM** address
**JOIN** customer ON address.address_id = customer.address_id
**WHERE** customer.store_id = 1 AND (address.city_id = 1 OR address.city_id = 42 OR address.city_id = 312 OR address.city_id = 459);


### ===== QUERY 5 ===== ###  
**Goal:**  What query would you run to get all the films with a "rating = G" and 
"special feature = behind the scenes", joined by actor_id = 15? Your query should 
return the film title, description, release year, rating, and special feature. 
Hint: You may use LIKE function in getting the 'behind the scenes' part.  
  
**SELECT** film.title, film.description, film.release_year, film.rating, film.special_features  
**FROM** film  
**JOIN** film_actor  
**ON** film.film_id = film_actor.film_id  
**WHERE** film_actor.actor_id = 15 AND film.rating = "G" AND film.special_features LIKE "%Behind the Scenes";  


### ===== QUERY 6 ====== ###
**Goal:**  What query would you run to get all the actors that joined in 
the film_id = 369? Your query should return the film_id, title, actor_id, 
and actor_name.  
  
**SELECT** film.film_id, film.title, film_actor.actor_id, actor.first_name, actor.last_name  
**FROM** film_actor  
**JOIN** film  
**ON** film_actor.film_id = film.film_id  
**JOIN** actor  
**ON** film_actor.actor_id = actor.actor_id  
**WHERE** film_actor.film_id = 369;  


### ===== QUERY 7 ====== ###
**Goal:** What query would you run to get all drama films with a rental rate of 
2.99? Your query should return film title, description, release year, rating, 
special features, and genre (category).  
  
**SELECT** film.title, film.description, film.release_year, film.rating, film.special_features, category.name  
**FROM** film_category  
**JOIN** film  
**ON** film_category.film_id = film.film_id  
**LEFT JOIN** category  
**ON** film_category.category_id = category.category_id  
**WHERE** film.rental_rate = 2.99 AND category.name = 'drama'  


### ===== QUERY 8 ===== ###
**Goal:** What query would you run to get all the action films which are joined 
by SANDRA KILMER? Your query should return film title, description, 
release year, rating, special features, genre (category), and actor's 
first name and last name.  
  
**SELECT** film.title, film.description, category.name, film.release_year, film.rating, film.special_features, actor.first_name, actor.last_name  
**FROM** film_actor  
**JOIN** film  
**ON** film_actor.film_id = film.film_id  
**JOIN** actor  
**ON** film_actor.actor_id = actor.actor_id  
**JOIN** film_category  
**ON** film_actor.film_id = film_category.film_id  
**LEFT JOIN** category  
**ON** film_category.category_id = category.category_id  
**WHERE** actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER' AND category.name = 'Action';