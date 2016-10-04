import Media
import fresh_tomatoes

# Set The movies Info
toy_story = Media.Movie("Toy Story"," A Story of a boy ","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","trailer")
avatar = Media.Movie("Avatar"," A marine with alien ","https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg","trailer")
Road_to_kabul = Media.Movie("Road to kabuL"," Quatre amis voulant se rendre en Hollande se retrouvent perdus en Afghanistan ! ","http://www.streamingplus.tv/gold-app/gold-uploads/media/road-to-kabul.jpg","trailer")
Zero = Media.Movie("Zero","Amin Bertale, a troubled cop, senses the futility and loss around him and tries to turn his life around.","http://fr.web.img2.acsta.net/pictures/210/561/21056180_20131115101544931.jpg","trailer")
Casanegra = Media.Movie("Casanegra","Casanegra is a 2008 Arabic-language Moroccan film acting in Casablanca by Nour Eddine","https://mrmorocco18.files.wordpress.com/2011/02/casanegra.png","trailer")
Horses_of_God = Media.Movie("Horses of God","After a stint in prison, a young man (Abdelilah Rachid) becomes a violent Islamic fundamentalist and recruits his younger brother (Abdelhakim Rachi) and the youth's best friend (Hamza Souidek) to his cause.","http://t0.gstatic.com/images?q=tbn:ANd9GcRQRn746ZY8zxrEwRImh6DH4vkitlIQQjCs_1gwvXia27ivtSUn","trailer")


# Store all the movies into a  lisr
movies = [Road_to_kabul,Horses_of_God,Casanegra,toy_story,avatar,Zero]
# Create a Website for those movies
fresh_tomatoes.open_movies_page(movies)
