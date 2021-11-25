import discord
import numpy
# from fun import *

responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes -         definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Dont count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.",
             "Very doubtful.""No... I mean yes... Well... Ask again later", "The answer is unclear... Seriously I double checked""It's a coin flip really...", "Yes, he will... Sorry I wan't really listening", "I could tell you but I'd have to permanently ban you", "Yes, No, Maybe... I don't know, could you repeat the question?", "YesNoYesNoYesNoYesNoYesNo ", "Ask yourself this question in the mirror three times", "the answer will become clear"]


people_embed = discord.Embed(title="List", colour=discord.Colour.random())
people_embed.add_field(name="People",
                       value="<@850708579614064692> -Jay Vardhan \n<@781376816295575552> -Vishnu \n<@910914620598919229> -Vijna \n<@806523983113093141> -Kartikeya\n<@785862484221231104> -Shreyas\n<@844934159561916497> -Aneesh\n<@725957400217255977> -Naren\n<@724321797301862461> -Jaswanth \n<@849929369325666334> -Vallab\n<@562547610649624587> -Gutta Sathvik \n<@747303289875595285> -CH Karthik \n<@800695986589794304> -Ujwal \n<@556777979821162496> -Pranav Karthik \n<@908346306672594954> -Aditya \n<@703197742989836399> -Naren Pillai \n<@765582119467876372> -Srihari \n<@911303709970034698> -Aastha \n<@761240819143278642> -Prakruthi \n<@762257391168258099> -Nishtha \n<@874897577739436074> -Kriti",
                       inline=False)


usernames = [
    "WebHunter#2714", "MemePepe#2455", "MadxxxVij208#2534",
    "KΛЯƬIKΣYΛ |On Break-Boards#5207", "steve-シュレーヤス#4569",
    "BLACK DEVIL#7714", "Camron なれん#2676", "don't mind#8430",
    "L0RDZUPR007#1677", "hellfirescorpio#2123", "no guess#5087",
    "ClappY#2816", "CR7#7293", "Nuclear#6281", "akuma{悪魔}#8897",
    "Heroic#7693", "aastha#6516", "piaa#9643", "Nish#0780"
]
ids = ["850708579614064692", "781376816295575552", "910914620598919229",
       "806523983113093141", "785862484221231104", "844934159561916497",
       "725957400217255977", "724321797301862461", "849929369325666334",
       "562547610649624587", "747303289875595285", "800695986589794304",
       "556777979821162496", "908346306672594954", "703197742989836399",
       "765582119467876372", "911303709970034698", "761240819143278642",
       "762257391168258099"]
names = ["Jay Vardhan", "Vishnu", "Vijna", "Kartikeya",
         "Shreyas", "Aneesh", "Naren", "Jaswanth", "Vallab",
         "Gutta Sathvik", "CH Karthik", "Ujwal", "Pranav Karhik", "Aditya",
         "Naren Pillai", "Srihari", "Aastha", "Prakruthi", "Nishta"]


# people_in_the_server="<@850708579614064692> -Jay Vardhan \n<@781376816295575552> -Vishnu \n<@910914620598919229> -Vijna \n<@806523983113093141> -Kartikeya\n<@785862484221231104> -Shreyas\n<@844934159561916497> -Aneesh\n<@725957400217255977> -Naren\n<@724321797301862461> -Jaswanth \n<@849929369325666334> -Vallab\n<@562547610649624587> -Gutta Sathvik \n<@747303289875595285> -CH Karthik \n<@800695986589794304> -Ujwal \n<@556777979821162496> -Pranav Karthik \n<@908346306672594954> -Aditya \n<@703197742989836399> -Naren Pillai \n<@765582119467876372> -Srihari \n<@911303709970034698> -Aastha \n<@761240819143278642> -Prakruthi \n<@762257391168258099> -Nishtha"


questions_for_truth = ["If your parents went out of town for a week and you had the house to yourself, what would you do?",
                       "What was the worst day of your life and why?",
                       "What was the weirdest/strangest dream you have ever had?",
                       "What is the one question you do not want to be asked in this game?",
                       "Rate everyone in this server, on a scale of one to ten.",
                       "List five disgusting/annoying habits you have?",
                       "What is your weight?",
                       "What is your height?",
                       "Have you ever stolen something?",
                       "Did you let someone else take the fall for something you did?",
                       "What was your childhood nickname?",
                       "What is the most embarrassing thing that your parents caught you do?",
                       "What was the stupidest thing you ever did?",
                       "How long have you gone without showering/shaving?",
                       "Did you ever pee in the swimming pool, while swimming?",
                       "Did you ever spread a nasty rumor about someone else?",
                       "What’s the weirdest thing you did when you were alone, in front of a mirror?",
                       "What kind of pajamas do you wear to bed?",
                       "What is the silliest thing that you are attached to and still posses (if it were a thing)?",
                       "Did you ever watch a R rated film and lie to your parents about it?",
                       "What was the biggest lie you told without getting caught?",
                       "Who is the one person you hate most in the world?",
                       "What do you do when you are alone at home?",
                       "Imagine this: you wake up one day and realize that you’ve become invisible. What will you do",
                       "If you had the chance to be reborn as someone in this server, who would it be?",
                       "What is your worst fear?",
                       "If you could be born again, what would you choose to be born as?",
                       "If you had just 24 hr to live, how would you spend your day?",
                       "If you had the chance to live on your own right now, would you take it?",
                       "What is the one thing you would change in your life if you had the option?",
                       "If you had one wish, what would you wish for?",
                       "If you knew that the world was going to end soon, what would you do?",
                       "If you were a superhero, what would your power be?",
                       "Would you rather be a princess/prince or a mermaid/hercules?",
                       "What would you do if you were the King/Queen of England?",
                       "Would you become the sex opposite to your gender for a day if you had the choice? Why?",
                       "Who was your first crush at school?",
                       "Who is the most handsome guy/beautiful girl at school?",
                       "Are you obsessed with a celebrity?",
                       "Did you ever lie to your best friend/bud?",
                       "What were your first impressions about “best friend’s name”?",
                       "Would you lie or cheat for a friend?",
                       "Name one quality that you do not like in your friend.",
                       "What do you like most about your best friend?",
                       "What are the three most important qualities you look for in a friend?",
                       "Who was the worst friend you have had and why?",
                       "What is the cruelest thing you have done to a friend?",
                       "Have you ever shared your best friend’s secrets with anyone else?",
                       "Can you go for weeks or even months without talking to your bestie?",
                       "Did you have an imaginary friend? What was his or her name?",
                       "Who is your favorite teacher and why?",
                       "Did you ever cheat in a test?",
                       "Which subject do you hate the most?",
                       "Which is the most boring class you had to attend?",
                       "Did you ever skip school by telling a lie and lie about it to your parents?",
                       "Did you ever mock a teacher or classmate behind their back?",
                       "What is the first thing you do after school every day?",
                       "What is your favorite thing to do at school?",
                       "Have you ever played a prank on a teacher?",
                       "How many times have you been punished and sent to the principal’s office?",
                       "Who is the creepiest kid you know in school?",
                       "What is the lowest/worst grade you got in school?",
                       "Have you ever fallen asleep in class?",
                       "Did you pretend to be sick so you can skip class or avoid a test?"
                       ]


questions_for_dare = ["add more dares to play"]

# , timestamp = ctx.message.created_at)
embed = discord.Embed(title='Commands', colour=discord.Colour.random())

embed.add_field(name='**.ping**',
                value='   -Check the bots latency.', inline=False)

embed.add_field(name='**.list**',
                value='   -Want to know the real name of someone on this server use this command to find out.', inline=False)

embed.add_field(name='**.nlearn**',
                value='   -Takes you to the Nlearn Website.', inline=False)

embed.add_field(name='**.chalam_sirs_channel **',
                value='   -Run it to see chalam sirs youtube channel and dont forget to watch rajamouli sirs dance.', inline=False)

embed.add_field(name='**.8ball**',
                value='   -Wanna know your future play 8ball to find it out.', inline=False)

embed.add_field(
    name='**.t**',
    value='   -Gives you a random truth answer it honestly.',
    inline=False)

embed.add_field(
    name='**.d**',
    value='   -Gives you a random dare "Just do it".',
    inline=False)
