from flask import Flask, render_template_string, render_template
# request, stream_with_context, Response
import time

app = Flask(__name__)

# adding password protection
# PASSPHRASE = "mariafernanda"

# MOVED BELOW 
# def generate_text(text):
#     for line in text:
#         for letter in line:
#             yield letter
#             print(end='')
#             time.sleep(0.1)  # Adjust the delay (in seconds) here
#         yield('<br>')
# MOVED BELOW

# adding a password protection
# def password_prompt(message):
#     return f'''
#                 <form action="/mensagens" method='post'>
#                   <label for="password">{message}:</label><br>
#                   <input type="password" id="password" name="password" value=""><br>
#                   <input type="submit" value="Submit">
#                 </form>'''

@app.route('/')
def index():
    return render_template('index.html')
    #return render_template('test.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/teach')
def teach():
    return render_template('teach.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

# uncomment for post method
@app.route('/mensagens') #, methods=['GET', 'POST'])
def print_text():

    text_to_print = ['(Filipa cada vez que me escribes que salta como un bichito en el estómago. Es terrible)', 'I want to fuck you.', 'Como amaneces?', 'eu também tenho sentimentos que são terríveis... e outros que são muito bons', 'Oye tu traduces lo que te escribo? Si no. Im very very impressed by your spanish knowledge', 'Es muy muy aparecido con Portuguese quando está escrito', 'Filipa yo me muero porque me enseñes muchas cosas ', 'Okay haha pero primero aprendes Python. Una idioma a la vez', 'Why am I so attracted to you? ', 'I don’t know. Why am I so attracted to you?', 'Filipa I had a dream with you ', 'I want you to tell me about your dreams slowly and in Spanish', 'Tu me encantas. Pero te lo voy a dejar de decir para que no se te suba a la cabeza ', 'I’ll teach you a lot', 'You make me feel unstable and not safe hahaha but it’s ok. I’m in for the learning ride and curve ', 'Don’t stop telling me. Unless you stop feeling it', 'Se feliz brilla mucho no enamores a mucha gente por ahí y muchos besos ', 'És linda ', 'Eres terrible ', 'Cannot stop thinking of you. I know you don’t like texting but wanted to say', 'Que rico. On your chair', 'You on top of me', 'I don’t want what happen to me last night to happen again', 'You’re an amazing and beautiful person and I hope you will be happy', 'Ojalá lo puedas hacer con una ética de cuidado que no sea solo ser nice sino de verdad pensar en quien entra en tus afectos, que además son jerárquicos, entonces igual hay desigualdades ', 'I still disagree with you. I think we could have something beautiful. But I can see you’re already letting go. ', '(Completely apart from that. I need to say something. You made me feel invisible and small yesterday, picked a bad time to tell me your stuff, it was like you couldn’t care less I was there. I know it’s not entirely like that and probably not your intention. But yea)', 'You’ll make some girl very happy ', 'Siento que hubiéramos podido tener algo muy chèvre. Lastima que todo se desmoronara tan rápido. Quizá no era para nosotras. Yo también espero nos crucemos por ahí ', 'The wheel of fortune keeps turning ', 'Yo entré en la situación con conocimiento y tengo que tomar responsabilidad de mis decisiones.', 'I cannot stop thinking of you here in bed with me', 'Me quiero arrunchar contigo en una hamaca en algún lado de Suramérica', 'My nipples are a little sore today', 'Es que me gustas mucho. Teach me how to be softer ', 'Estou bem. Pensando em ti todo o tempo ', 'Oye eres muy tasty ', 'I’m going to save that photo ', 'What are you doing to me that I can’t stop thinking about you!? ', 'You can absolutely tell me your fears', 'They do, like cute bright insects ', 'Remember when you said my eyelashes look like mosquitos ', 'I keep thinking that we go to a party and dance super close and then we go outside to smoke (I know this place) and you push me against a wall and  finger me intensely and I get super wet and I kiss you so much ', 'So last night when I went to bed I touched myself and thought of you on top of me, moving very tight against me so I could feel everything. ', 'Because my secret plan is to get you to dance that song with me at a party bf you go? ', 'Please send me a fantasy before 3:22 (take off time) so I can dream about it', 'Don’t fall in love with strangers on the train ', 'We can change the rules and make better ones if we want ', 'My bed smelled a bit like you this morning and I melted', 'Why do I always want to play Otro Atardecer and think of you', 'I’m just afraid ', 'Ola María I know we agreed not to text but just want to say I really liked being with you last night :)', 'Me encanta cuando te estoy chupando y me miras me vuelve loca ', 'I’m afraid too', 'Me encantaría que sudaras encima mío ', 'I keep pinching my nipples and thinking of your mouth', 'Does it make you feel uncomfortable? ', 'Hope I wasn’t too heavy last night / this morning. ', 'It was intense but I like intense. I like you ', 'I want to fuck you with the strap. Cannot stop thinking about it', 'He estado pensando hoy que la verdad es que no me quiero apegar especialmente sabiendo que tu no puedes tener sentimientos por mi. Pero he disfrutado mucho lo que hemos tenido hasta ahora y tu compañía y tus besos. ', 'I’m thinking a lot about going down on you. I want you to sit on the edge of my bed while I do it. Then when you’re ready I would fuck you. ', 'Let’s talk in eternal present I love when people tell stories in present tense. ', 'You’re beautiful and make me very happy', 'I get big cards when I’m with you ', 'I always write in the present', 'I think we need to not talk during your vacation ', 'I think the reversal means that something from your past has collapsed but you haven’t dealt with it. ', 'It’s not what I truly truly want I’m trying to test some limits and have space so we can idk think in cold waters ', '(Also I cannot stop thinking about you fucking me. Intrusive flashbacks. All the positions. You’re so hot) ', 'Yo también te estoy pensando mucho, sigo pensando en nuestra última noche: tú encima de mi ', '🥵 ', 'Sorry if I said something that made you feel bad. I just wanted to express how I felt. But that doesn’t take away that I had a great time with you and appreciate your energy and your presence a lot; and I know you were hurting too. ', 'I really like how you kiss me in the middle of the night ', 'Hola te pienso mucho quisiera verte, solo quería que lo supieras, espero estes feliz abrazo ', 'Honestly I feel so terrible. It feels like another breakup. I know you don’t want to talk at all but it sounds so harsh to me', 'I mean if you want to talk about this kind of things I’m down anytime ', 'Ay one more thing. I cannot stop thinking of your body, the things you say, and you being under me. I want it all', 'Y también pensé que estabas parada y yo te pasaba toda la lengua entre tus piernas y te comía muy rico ', 'It was nice to hear your voice. Today I’m feeling crushed - not going to lie. But I respect your process and don’t want to cause you more pain. Wishing you the best Maria', 'Filipaaaaa you will kill me i know ', 'I have hope but I won’t pressure you, I can wait and I may be crushed again but that’s okay ', 'I was thinking about the last night we were together and you were on top of me and I had my fingers inside you and the way you moved it was so hot, you made me go crazy ', 'More specifically, I want to fall asleep with you then wake you up in the middle of the night and fuck you slowly', 'Hola Filipa. It’s ok. You’ve said this before, that you won’t bring it up but it keeps happening. Actually you told me the same story twice. You had already mentioned las time that she reached out. And again, you told me a level of details this time that I didn’t ask for. And the first time we spoke on the phone I interrupted you and asked you to please don’t talk about it anymore. But probably you don’t remember any of this. Seems like you are not present. At least not with me. I don’t want what you are offering. ', 'Quiero que me comias muy rico', 'You broke my heart but it was my mistake ', 'I want to see your eyes looking up at me when you do', 'I want you and want to smash your porcelain. ', 'You’re the only reason I want to go back ', 'Lo que hablamos, tu voz, lo que quiero hacerte y que me hagas. Y me acordaba de estar en tu cama y cuando me dices “come lay down” and you don’t let me eat you twice, me dices “stop come lay down” and I like it but I want more.', 'I think next time you might come with me. Perhaps', 'Te acuerdas cuando me diste un muffin como premio de consolación y me dijiste i can’t have anything with you.', 'Hope you can move forward ', 'And it’s a game I’ve learned from childhood, always going for the person that won’t give love back.', 'But you’re also wrong. It was my mistake too. I should have talked to you about what it was like from your side to be with someone unavailable. I should have been more responsible but I couldn’t do it back then ']

    def generate_text(text):
        for line in text:
            for letter in line:
                yield letter
                print(end='')
                time.sleep(0.1)
            yield('<br>')

    return generate_text(text_to_print)
    # if request.method == 'GET':
    #     return password_prompt("Enter password")
    # elif request.method == 'POST':
    #     if request.form['password'] != PASSPHRASE:
    #         return password_prompt("Invalid password, try again.")
    #     else:
    #         # nesting a generator within an outer function to help
    #         # streaming?
    #         # https://www.pythonanywhere.com/forums/topic/28503/ 
            # def generate_text(text):
            #     for line in text:
            #         for letter in line:
            #             yield letter
            #             print(end='')
            #             time.sleep(0.1)  # Adjust the delay (in
            #             # seconds) here
            #         yield('<br>')
            #     return generate_text(text_to_print)
            
            # response = Response(stream_with_context(generate_text(text_to_print)))
    # response.headers['X-Accel-Buffering'] = 'no'
    # return response


if __name__ == '__main__':
    app.run(debug=True)

