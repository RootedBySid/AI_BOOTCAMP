import wordcloud 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter


text = '''Technology is changing the world at an incredible pace. Every day, new technology creates new opportunities for learning, communication, business, and innovation. Artificial intelligence, machine learning, cybersecurity, cloud computing, and software development are becoming important parts of modern life. Artificial intelligence helps computers understand information, recognize patterns, generate content, and solve complex problems. Machine learning allows systems to learn from data and improve their performance over time. Cybersecurity protects computers, networks, applications, and personal information from attacks and threats. Cloud computing allows people and organizations to store data and run applications without depending entirely on local computers. Software development brings these technologies together to create useful applications and services.

Learning technology requires curiosity, consistency, and practical experience. Programming languages such as Python, Java, C++, and JavaScript help developers build different kinds of software. Projects provide an opportunity to turn theoretical knowledge into practical skills. Debugging teaches patience, while experimentation encourages creativity. The technology industry continues to evolve, creating new careers and challenges every year. Students who keep learning, building projects, solving problems, and understanding new technologies can adapt to this rapidly changing environment. The future will depend on people who can combine technical knowledge, creativity, security, and responsible innovation to build technology that is useful, reliable, and accessible.
'''


words = word_tokenize(text.lower())
# print(words)

word_frequencies = Counter(words)
# print(word_frequencies)


wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords.words('english')).generate_from_frequencies(word_frequencies)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
plt.savefig('wordcloud.png', bbox_inches='tight')