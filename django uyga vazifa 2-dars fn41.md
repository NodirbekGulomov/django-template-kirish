1-topshiriq: youtubeda html va css ga oid videolarni koring va organing

2-topshiriq:

Siz Django yordamida kitoblar ma’lumotini view’dan olib template’da jadval ko‘rinishida chiqaradigan oddiy project qilishingiz kerak.

Bunda kitoblar ro‘yxatini view ichida Python list/dict ko‘rinishida saqlaysiz va shu ma’lumotlarni template’ga yuborasiz. Template ichida esa Django for loop orqali barcha kitoblarni jadval (table) ko‘rinishida chiqarasiz.

Jadvalga CSS yordamida chiroyli dizayn bering. CSS alohida static fayl orqali ulanadi.

Quyidagi kitoblar listidan view ichida foydalaning:

books \= \[  
   {  
       "id": 1,  
       "title": "Clean Code",  
       "author": "Robert C. Martin",  
       "price": 120,  
       "description": "A handbook of agile software craftsmanship"  
   },  
   {  
       "id": 2,  
       "title": "The Pragmatic Programmer",  
       "author": "Andrew Hunt",  
       "price": 95,  
       "description": "Journey to mastery in software development"  
   },  
   {  
       "id": 3,  
       "title": "Design Patterns",  
       "author": "Erich Gamma",  
       "price": 150,  
       "description": "Reusable object-oriented design solutions"  
   },  
   {  
       "id": 4,  
       "title": "You Don’t Know JS",  
       "author": "Kyle Simpson",  
       "price": 80,  
       "description": "Deep dive into JavaScript core concepts"  
   },  
   {  
       "id": 5,  
       "title": "Fluent Python",  
       "author": "Luciano Ramalho",  
       "price": 110,  
       "description": "Clear, concise Python programming guide"  
   }  
\]

Natijada bitta sahifada kitoblar chiroyli jadval ko‘rinishida chiqishi kerak va barcha ma’lumotlar view’dan kelgan bo‘lishi shart (HTML ichida hardcode ma’lumot yozilmaydi).

