#!/usr/bin/python
# coding=utf-8

import os.path
import random
import numpy

def strip_non_ascii(string):
	""" Returns the string without non ASCII characters """
	stripped = (c for c in string if 0 < ord(c) < 127)
	return ''.join(stripped)

def scrambled(orig):
	""" Scramble a dictionary """
	dest = orig[:]
	random.shuffle(dest)
	return dest

types_of_text = {
	'scifi': """In a world deep down in Smallness, in an electron of a dead cell of apiece of wood, five scientists were grouped before a complicatedinstrument with a horn like the early radios. Two sat and three stood,but their attention upon the apparatus was unanimous. From smallhollowed cups worn on their fingers like rings, came a smoke fromburning incense. These cups they held to their noses frequently, andtheir eyes shone as they inhaled. The scientists of infra smallness weresmoking!With the exception of a recent prolonged silence, which was causing themgreat anxiety, sounds had been issuing from the instrument for days.There had been breaks before, but this silence had been long enduring.Now the voice was speaking again; a voice that was a telepathiccommunication made audible. The scientists brightened."There is much that I cannot understand," it said. The words werehesitant, filled with awe. "I seem to have been in many worlds. At thecompletion of my experiment, I stood on a land which was brown and blackand very rough of surface. With startling suddenness, I was propelledacross this harsh country, and, terrifyingly, I was falling. I must havedropped seventy five feet, but the strange buoyant atmosphere of thisstrange world saved me from harm."My new surroundings were grey and gloomy, and the earth trembled as agiant cloud passed over the sky. I do not know what it meant, but withthe suddenness characteristic of this place, it became very dark, and aninexplicable violence shook me into insensibility."I am conscious, now, of some giant form before me, but it is socolossal that my eyes cannot focus it. And it changes. Now I seemconfronted by great orange mountains with curving ledges cut into theirsides. Atop them are great, greyish slabs of protecting opaque rock  acovering like that above our Temples of Aerat  'on which the rain maynever fall.' I wish that you might communicate with me, good men of myworld. How go the Gods?"But now! These mountains are lifting, vanishing from my sight. A great thing  which I cannot comprehend hovers before me. It has many colors,but mostly there is the orange of the mountains. It hangs in the air,and from the portion nearest me grow dark trees as round as myself andas tall. There is a great redness above, that opens like the Katusflower, exposing the ivory white from which puffs the Tongue of Death.Beyond this I cannot see well, but ever so high are two gigantic cavernsfrom which the Winds of the Legends blow  and suck. As dangerous as theKatus, by Dal! Alternately they crush me to the ground, then threaten totear me from it and hurl me away." My nose was the cavern from which issued the horrifying wind. I noticedthat my breath distressed the little man as I leaned over to stare athim, so drew back.  Upstairs, the visor buzzed. Before answering, so that I would not losethe little man, I very gingerly pinched his shirt with the tongs, andlifted him to the table. "My breath! I am shot into the heavens like Milo and his rocket! Itraverse a frightful distance! Everything changes constantly. A millionmiles below is chaos. This world is mad! A giant landscape passesbeneath me, so weird I cannot describe it. I  I cannot understand. Onlymy heart trembles within me. Neither Science nor the gods can help orcomfort in this awful world of Greatness!"We stop. I hang motionless in the air. The ground beneath is utterlyinsane. But I see vast uncovered veins of rare metal  and crystal,precious crystal, enough to cover the mightiest Temple we could build!Oh, that Mortia were so blessed! In all this terrifying world, therichness of the crystal and the marvelous metal do redeem."Men!    I see ... I believe it is a temple! It is incredibly tall, ofblack foundation and red spire, but it is weathered, leaning as if tofall  and very bare. The people cannot love their Gods as we  or elsethere is the Hunger.... But the gods may enlighten this world, too, andif lowered, I will make for it. A sacred Temple should be ahaven  friends! I descend." The little man's eye had caught my scissors and a glass ruler as Isuspended him above my desk. They were his exposed vein of metal and theprecious crystal. I was searching for something to secure him. In thelast second before I lowered him, his heart swelled at the sight of the"Temple"  my red and black pen slanting upward from the desk holder.artinez drummed the desk top with nervous fingers. "I'll look into itif you insist," he said, "though it'll cost you a pretty penny. Richmen's lives aren't easy to pry into if they've got something they wantto hide. But I don't think we'd find out much; your case seems to beonly one of a rash of similar ones in the past year.""Huh?" Fraser looked sharply up."Yeah. I follow all the news; and remember the odd facts. There've beena good dozen cases recently, where beautiful young women suddenlymarried rich men or became their mistresses. It doesn't all get into thepapers, but I've got my contacts. I know. In every instance, there wasno obvious reason; in fact, the dames seemed very much in love withdaddy.""And the era of the gold digger is pretty well gone  " Fraser satstaring out the window. It didn't seem right that the sky should be sofull of sunshine."Well," said Martinez, "you don't need me. You need a psychologist." Psychologist! "By God, Juan, I'm going to give you a job anyway!" Fraser leaped to hisfeet. "You're going to check into an outfit called Sentiment, Inc."                                        A week later, Martinez said, "Yeah, we found it easily enough. It's notin the phone book, but they've got a big suite right in the high rentdistrict on Fifth. The address is here, in my written report. Nobody inthe building knows much about 'em, except that they're a quiet,well behaved bunch and call themselves research psychologists. They havea staff of four: a secretary receptionist; a full time secretary; and acouple of husky boys who may be bodyguards for the boss. That's thisKennedy, Robert Kennedy. My man couldn't get into his office; the girlsaid he was too busy and never saw anybody except some regular clients.Nor could he date either of the girls, but he did investigate them."The receptionist is just a working girl for routine stuff, married,hardly knows or cares what's going on. The steno is unmarried, has adegree in psych, lives alone, and seems to have no friends except herboss. Who's not her lover, by the way.""Well, how about Kennedy himself?" asked Fraser."I've found out a good bit, but it's all legitimate," said Martinez."He's about fifty years old, a widower, very steady private life. He's alicensed psychiatrist who used to practice in Chicago, where he also didresearch in collaboration with a physicist named Gavotti, who's sincedied. Shortly after that happened  "No, there's no suspicion of foul play; the physicist was an old man anddied of a heart attack. Anyway, Kennedy moved to New York. He stillpractices, officially, but he doesn't take just anybody; claims that hisresearch only leaves him time for a few." Martinez narrowed his eyes."The only thing you could hold against him is that he occasionally seesa guy named Bryce, who's in a firm that has some dealings with Amtorg.""The Russian trading corporation? Hm.""Oh, that's pretty remote guilt by association, Colin. Amtorg does havelegitimate business, you know. We buy manganese from them, among otherthings. And the rest of Kennedy's connections are all strictly blueribbon.  Crème de la crème   business, finance, politics, and one bigunion leader who's known to be a conservative. In fact, Kennedy'sfriends are so powerful you'd have real trouble doing anything againsthim."Fraser slumped in his chair. "I suppose my notion was pretty wild," headmitted."Well, there is one queer angle. You know these rich guys who'vesuddenly made out with such highly desirable dames? As far as I couldfind out, every one of them is a client of Kennedy's.""Eh?" Fraser jerked erect."'S a fact. Also, my man showed the building staff, elevator pilots andso on, pictures of these women, and a couple of 'em were remembered ashaving come to see Kennedy."It was the light touch of the boy An upon my shoulder which roused me.He was bending down, his pretty face full of concernful sympathy, andin a minute said  knowing nothing of my thoughts, of course."It is the wine, stranger, the pink oblivion, it sometimes makes onefeel like that until enough is taken; you stopped just short of whatyou should have had, and the next cup would have been delight  I shouldhave told you.""Ay," I answered, glad he should think so, "it was the wine, no doubt;your quaint drink, sir, tangled up my senses for the moment, but theyare clearer now, and I am eager past expression to learn a little moreof this strange country I have wandered into.""I would rather," said the boy, relapsing again into his state ofkindly lethargy, "that you learnt things as you went, for talking iswork, and work we hate, but today we are all new and fresh, and if everyou are to ask questions now is certainly the time.  Come with me tothe city yonder, and as we go I will answer the things you wish toknow;" and I went with him, for I was humble and amazed, and, in truth,at that moment, had not a word to say for myself.All the way from the plain where I had awoke to the walls of the citystood booths, drinking places, and gardens divided by labyrinths ofcanals, and embowered in shrubberies that seemed coming into leaf andflower as we looked, so swift was the process of their growth. Thesewaterways were covered with skiffs being pushed and rowed in everydirection; the cheerful rowers calling to each other through the leafyscreens separating one lane from another till the place was full oftheir happy chirruping.  Every booth and way side halting place wasthronged with these delicate and sprightly people, so friendly, sogracious, and withal so purposeless.I began to think we should never reach the town itself, for first myguide would sit down on a green stream bank, his feet a dangle in theclear water, and bandy wit with a passing boat as though there werenothing else in the world to think of.  And when I dragged him out ofthat, whispering in his ear, "The town, my dear boy! the town!  I amall agape to see it," he would saunter reluctantly to a booth a hundredyards further on and fall to eating strange confections or sippingcoloured wines with chance acquaintances, till again I plucked him bythe sleeve and said: "Seth, good comrade  was it not so you called yourcity just now?  take me to the gates, and I will be grateful to you,"then on again down a flowery lane, aimless and happy, wasting my timeand his, with placid civility I was led by that simple guide.""",
	'philosophy': """
	We should not deck out and embellish Christianity: it has waged a war to the death against this higher type of man, it has put all the deepest instincts of this type under its ban, it has developed its concept of evil, of the Evil One himself, out of these instincts the strong man as the typical reprobate, the  outcast among men   Christianity has taken the part of all the weak, the low, the botched; it has made an ideal out of antagonism to all the self preservative instincts of sound life; it has corrupted even the faculties of those natures that are intellectually most vigorous, by representing the highest intellectual values as sinful, as misleading, as full of temptation  The most lamentable example: the corruption of Pascal, who believed that his intellect had been destroyed by original sin, whereas it was actually destroyed by Christianity! 6 It is a painful and tragic spectacle that rises before me: I have drawn back the curtain from the rottenness of man  This word, in my mouth,  is at least free from one suspicion: that it involves a moral accusation against humanity  It is used and I wish to emphasize the fact again without any moral significance: and this is so far true that the rottenness I speak of is most apparent to me precisely in those quarters where there has been most aspiration, hitherto, toward  virtue  and  godliness   As you probably surmise, I understand rottenness in the sense of décadence: my argument is that all the values on which mankind now fixes its highest aspirations are décadence values I call an animal, a species, an individual corrupt, when it loses its instincts, when it chooses, when it prefers, what is injurious to it  A history of the  higher feelings,  the  ideals of humanity  and it is possible that I’ll have to write it would almost explain why man is so degenerate  Life itself appears to me as an instinct for growth, for survival, for the accumulation of forces, for power: whenever the will to power fails there is disaster  My contention is that all the highest values of humanity have been emptied of this will that the values of décadence, of nihilism, now prevail under the holiest names  7 Christianity is called the religion of pity  Pity stands in opposition to all the tonic passions that augment the energy of the feeling of aliveness: it is a depressant  A man loses power when he pities  Through pity that drain upon strength which suffering works is multiplied a thousandfold  Suffering is made contagious by pity; under certain circumstances it may lead to a total sacrifice of life and living energy a loss out of all proportion to the magnitude of the cause   the case of the death of the Nazarene)  This is the first view of it; there is, however, a still more important one  If one measures the effects of pity by the gravity of the reactions it sets up, its character as a menace to life appears in a much clearer light  Pity thwarts the whole law of evolution, which is the law of natural selection  It preserves whatever is ripe for destruction; it fights on the side of those disinherited and condemned by life; by maintaining life in so many of the botched of all kinds, it gives life itself a gloomy and dubious aspect  Mankind has ventured to call pity a virtue   in every superior moral  system it appears as a weakness ; going still further, it has been called the virtue, the source and foundation of all other virtues but let us always bear in mind that this was from the standpoint of a philosophy that was nihilistic, and upon whose shield the denial of life was inscribed  Schopenhauer was right in this: that by means of pity life is denied, and made worthy of denial pity is the technic of nihilism  Let me repeat: this depressing and contagious instinct stands against all those instincts which work for the preservation and enhancement of life: in the rôle of protector of the miserable, it is a prime agent in the promotion of décadence pity persuades to extinction     Of course, one doesn’t say  extinction : one says  the other world,  or  God,  or  the true life,  or Nirvana, salvation, blessedness     This innocent rhetoric, from the realm of religious ethical balderdash, appears a good deal less innocent when one reflects upon the tendency that it conceals beneath sublime words: the tendency to destroy life  Schopenhauer was hostile to life: that is why pity appeared to him as a virtue     Aristotle, as every one knows, saw in pity a sickly and dangerous  state of mind, the remedy for which was an occasional purgative: he regarded tragedy as that purgative  The instinct of life should prompt us to seek some means of puncturing any such pathological and dangerous accumulation of pity as that appearing in Schopenhauer’s case  and also, alack, in that of our whole literary décadence, from St  Petersburg to Paris, from Tolstoi to Wagner), that it may burst and be discharged     Nothing is more unhealthy, amid all our unhealthy modernism, than Christian pity  To be the doctors here, to be unmerciful here, to wield the knife here all this is our business, all this is our sort of humanity, by this sign we are philosophers, we Hyperboreans! 8 It is necessary to say just whom we regard as our antagonists: theologians and all who have any theological blood in their veins this is our whole philosophy     One must have faced that menace at close hand, better still, one must have had experience of it directly and almost succumbed to it, to realize that it is not to be taken lightly   the alleged free thinking of our  naturalists and physiologists seems to me to be a joke they have no passion about such things; they have not suffered   This poisoning goes a great deal further than most people think: I find the arrogant habit of the theologian among all who regard themselves as  idealists  among all who, by virtue of a higher point of departure, claim a right to rise above reality, and to look upon it with suspicion     The idealist, like the ecclesiastic, carries all sorts of lofty concepts in his hand   and not only in his hand!); he launches them with benevolent contempt against  understanding,   the senses,   honor,   good living,   science ; he sees such things as beneath him, as pernicious and seductive forces, on which  the soul  soars as a pure thing in itself as if humility, chastity, poverty, in a word, holiness, had not already done much more damage to life than all imaginable horrors and vices     The pure soul is a pure lie     So long as the priest, that professional denier, calumniator and poisoner of life, is accepted as a higher variety of man, there can be no answer to the question, What is truth? Truth has already been stood on its head when the obvious attorney of  mere emptiness is mistaken for its representative    9 Upon this theological instinct I make war: I find the tracks of it everywhere  Whoever has theological blood in his veins is shifty and dishonourable in all things  The pathetic thing that grows out of this condition is called faith: in other words, closing one’s eyes upon one’s self once for all, to avoid suffering the sight of incurable falsehood  People erect a concept of morality, of virtue, of holiness upon this false view of all things; they ground good conscience upon faulty vision; they argue that no other sort of vision has value any more, once they have made theirs sacrosanct with the names of  God,   salvation  and  eternity   I unearth this theological instinct in all directions: it is the most widespread and the most subterranean form of falsehood to be found on earth  Whatever a theologian regards as true must be false: there you have almost a criterion of truth  His profound instinct of self preservation stands against truth ever coming into honour in any way, or even getting stated  Wherever the in fluence of theologians is felt there is a transvaluation of values, and the concepts  true  and  false  are forced to change places: whatever is most damaging to life is there called  true,  and whatever exalts it, intensifies it, approves it, justifies it and makes it triumphant is there called  false      When theologians, working through the  consciences  of princes  or of peoples , stretch out their hands for power, there is never any doubt as to the fundamental issue: the will to make an end, the nihilistic will exerts that power    10 Among Germans I am immediately understood when I say that theological blood is the ruin of philosophy  The Protestant pastor is the grandfather of German philosophy; Protestantism itself is its peccatum originale  Definition of Protestantism: hemiplegic paralysis of Christianity and of reason     One need only utter the words  Tübingen School  to get an understanding of what German philosophy is at bottom a very artful form of theology     The Suabians are the best liars in Germany; they lie innocently     Why all  the rejoicing over the appearance of Kant that went through the learned world of Germany, three fourths of which is made up of the sons of preachers and teachers why the German conviction still echoing, that with Kant came a change for the better? The theological instinct of German scholars made them see clearly just what had become possible again     A backstairs leading to the old ideal stood open; the concept of the  true world,  the concept of morality as the essence of the world   the two most vicious errors that ever existed!), were once more, thanks to a subtle and wily scepticism, if not actually demonstrable, then at least no longer refutable     Reason, the prerogative of reason, does not go so far     Out of reality there had been made  appearance ; an absolutely false world, that of being, had been turned into reality     The success of Kant is merely a theological success; he was, like Luther and Leibnitz, but one more impediment to German integrity, already far from steady  11 A word now against Kant as a moralist  A virtue must be our invention; it must spring out  of our personal need and defence  In every other case it is a source of danger  That which does not belong to our life menaces it; a virtue which has its roots in mere respect for the concept of  virtue,  as Kant would have it, is pernicious   Virtue,   duty,   good for its own sake,  goodness grounded upon impersonality or a notion of universal validity these are all chimeras, and in them one finds only an expression of the decay, the last collapse of life, the Chinese spirit of Königsberg  Quite the contrary is demanded by the most profound laws of self preservation and of growth: to wit, that every man find his own virtue, his own categorical imperative  A nation goes to pieces when it confounds its duty with the general concept of duty  Nothing works a more complete and penetrating disaster than every  impersonal  duty, every sacrifice before the Moloch of abstraction  To think that no one has thought of Kant’s categorical imperative as dangerous to life!    The theological instinct alone took it under protection! An action prompted by the life instinct proves that it is a right action by the amount of pleasure that goes with it: and yet that Nihilist, with his bowels  of Christian dogmatism, regarded pleasure as an objection     What destroys a man more quickly than to work, think and feel without inner necessity, without any deep personal desire, without pleasure as a mere automaton of duty? That is the recipe for décadence, and no less for idiocy     Kant became an idiot  And such a man was the contemporary of Goethe! This calamitous spinner of cobwebs passed for the German philosopher still passes today!    I forbid myself to say what I think of the Germans     Didn’t Kant see in the French Revolution the transformation of the state from the inorganic form to the organic? Didn’t he ask himself if there was a single event that could be explained save on the assumption of a moral faculty in man, so that on the basis of it,  the tendency of mankind toward the good  could be explained, once and for all time? Kant’s answer:  That is revolution   Instinct at fault in everything and anything, instinct as a revolt against nature, German décadence as a philosophy that is Kant!  12 I put aside a few sceptics, the types of decency in the history of philosophy: the rest haven’t the slightest conception of intellectual integrity  They behave like women, all these great enthusiasts and prodigies they regard  beautiful feelings  as arguments, the  heaving breast  as the bellows of divine inspiration, conviction as the criterion of truth  In the end, with  German  innocence, Kant tried to give a scientific flavour to this form of corruption, this dearth of intellectual conscience, by calling it  practical reason   He deliberately invented a variety of reasons for use on occasions when it was desirable not to trouble with reason that is, when morality, when the sublime command  thou shalt,  was heard  When one recalls the fact that, among all peoples, the philosopher is no more than a development from the old type of priest, this inheritance from the priest, this fraud upon self, ceases to be remarkable  When a man feels that he has a divine mission, say to lift up, to save or to liberate mankind when a man feels the divine spark in his heart and believes that he is the mouthpiece of super natural imperatives when such a mission inflames him, it is only natural that he should stand beyond all merely reasonable standards of judgment  He feels that he is himself sanctified by this mission, that he is himself a type of a higher order!    What has a priest to do with philosophy! He stands far above it! And hitherto the priest has ruled! He has determined the meaning of  true  and  not true !   13 Let us not underestimate this fact: that we ourselves, we free spirits, are already a  transvaluation of all values,  a visualized declaration of war and victory against all the old concepts of  true  and  not true   The most valuable intuitions are the last to be attained; the most valuable of all are those which determine methods  All the methods, all the principles of the scientific spirit of today, were the targets for thousands of years of the most profound contempt; if a man inclined to them he was excluded from the society of  decent  people he passed as  an enemy of God,  as a scoffer at the truth, as one  possessed   As  a man of science, he belonged to the Chandala[2]     We have had the whole pathetic stupidity of mankind against us their every notion of what the truth ought to be, of what the service of the truth ought to be their every  thou shalt  was launched against us     Our objectives, our methods, our quiet, cautious, distrustful manner all appeared to them as absolutely discreditable and contemptible  Looking back, one may almost ask one’s self with reason if it was not actually an aesthetic sense that kept men blind so long: what they demanded of the truth was picturesque effectiveness, and of the learned a strong appeal to their senses  It was our modesty that stood out longest against their taste     How well they guessed that, these turkey cocks of God![2] The lowest of the Hindu castes 14 We have unlearned something  We have become more modest in every way  We no longer derive man from the  spirit,  from the  godhead ; we have dropped him back among the beasts  We regard him as the strongest of the beasts because he is the craftiest; one of the re sults thereof is his intellectuality  On the other hand, we guard ourselves against a conceit which would assert itself even here: that man is the great second thought in the process of organic evolution  He is, in truth, anything but the crown of creation: beside him stand many other animals, all at similar stages of development     And even when we say that we say a bit too much, for man, relatively speaking, is the most botched of all the animals and the sickliest, and he has wandered the most dangerously from his instincts though for all that, to be sure, he remains the most interesting! As regards the lower animals, it was Descartes who first had the really admirable daring to describe them as machina; the whole of our physiology is directed toward proving the truth of this doctrine  Moreover, it is illogical to set man apart, as Descartes did: what we know of man today is limited precisely by the extent to which we have regarded him, too, as a machine  Formerly we accorded to man, as his inheritance from some higher order of beings, what was called  free will ; now we have taken even this will from him, for the term no longer describes anything that we can understand  The old word   will  now connotes only a sort of result, an individual reaction, that follows inevitably upon a series of partly discordant and partly harmonious stimuli the will no longer  acts,  or  moves      Formerly it was thought that man’s consciousness, his  spirit,  offered evidence of his high origin, his divinity  That he might be perfected, he was advised, tortoise like, to draw his senses in, to have no traffic with earthly things, to shuffle off his mortal coil then only the important part of him, the  pure spirit,  would remain  Here again we have thought out the thing better: to us consciousness, or  the spirit,  appears as a symptom of a relative imperfection of the organism, as an experiment, a groping, a misunderstanding, as an affliction which uses up nervous force unnecessarily we deny that anything can be done perfectly so long as it is done consciously  The  pure spirit  is a piece of pure stupidity: take away the nervous system and the senses, the so called  mortal shell,  and the rest is miscalculation that is all!    15 Under Christianity neither morality nor religion has any point of contact with actuality  It offers purely imaginary causes   God,   soul,   ego,   spirit,   free will  or even  unfree ), and purely imaginary effects   sin,   salvation,   grace,   punishment,   forgiveness of sins )  Intercourse between imaginary beings   God,   spirits,   souls ); an imaginary natural history  anthropocentric; a total denial of the concept of natural causes); an imaginary psychology  misunderstandings of self, misinterpretations of agreeable or disagreeable general feelings for example, of the states of the nervus sympathicus with the help of the sign language of religio ethical balderdash ,  repentance,   pangs of conscience,   temptation by the devil,   the presence of God ); an imaginary teleology  the  kingdom of God,   the last judgment,   eternal life )  This purely fictitious world, greatly to its disadvantage, is to be differentiated from the world of dreams; the latter at least reflects reality, whereas the former falsifies it, cheapens it and denies it  Once the concept of  nature  had  been opposed to the concept of  God,  the word  natural  necessarily took on the meaning of  abominable  the whole of that fictitious world has its sources in hatred of the natural   the real! , and is no more than evidence of a profound uneasiness in the presence of reality     This explains everything  Who alone has any reason for living his way out of reality? The man who suffers under it  But to suffer from reality one must be a botched reality     The preponderance of pains over pleasures is the cause of this fictitious morality and religion: but such a preponderance also supplies the formula for décadence    16 A criticism of the Christian concept of God leads inevitably to the same conclusion  A nation that still believes in itself holds fast to its own god  In him it does honour to the conditions which enable it to survive, to its virtues it projects its joy in itself, its feeling of power, into a being to whom one may offer thanks  He who is rich will give of his riches; a proud people need a god to whom they can make sacrifices     Religion, within these  limits, is a form of gratitude  A man is grateful for his own existence: to that end he needs a god  Such a god must be able to work both benefits and injuries; he must be able to play either friend or foe he is wondered at for the good he does as well as for the evil he does  But the castration, against all nature, of such a god, making him a god of goodness alone, would be contrary to human inclination  Mankind has just as much need for an evil god as for a good god; it doesn’t have to thank mere tolerance and humanitarianism for its own existence     What would be the value of a god who knew nothing of anger, revenge, envy, scorn, cunning, violence? who had perhaps never experienced the rapturous ardeurs of victory and of destruction? No one would understand such a god: why should any one want him? True enough, when a nation is on the downward path, when it feels its belief in its own future, its hope of freedom slipping from it, when it begins to see submission as a first necessity and the virtues of submission as measures of self preservation, then it must overhaul its god  He then becomes a hypocrite, timorous and demure; he counsels  peace of  soul,  hate no more, leniency,  love  of friend and foe  He moralizes endlessly; he creeps into every private virtue; he becomes the god of every man; he becomes a private citizen, a cosmopolitan     Formerly he represented a people, the strength of a people, everything aggressive and thirsty for power in the soul of a people; now he is simply the good god     The truth is that there is no other alternative for gods: either they are the will to power in which case they are national gods or incapacity for power in which case they have to be good    
	""",
}

class Analysis:
	def __init__(self, type_of_text):
		""" Opens the file and cleans it, then finds unique words """
		self.s = types_of_text[type_of_text]
		# This contains all of the words as a list.
		self.cleaned = [ n.lower() for n in strip_non_ascii(self.s).replace("\n","").split(" ") ]
		# Self explanatory.
		self.unique_words = list(set(self.cleaned))
		# Length so I don't have to reference multiple time later.
		self.t = len(self.unique_words)
		self.loaded = False
	def load(self):
		""" Loads data from the filename, should be called before any other method. """
		if not self.loaded:
			self.appearances = numpy.zeros( (self.t, self.t) )
			self.probabilities = numpy.zeros( ( self.t, 100 ) )
			self.count()
			self.normalize()
			self.generate_probabilities()
			self.loaded = True
	def count(self):
		"""
			For every word in the unique words:
				Counts how many times it is followed by every word that ever follows it.
			Saves result in appearances.
		"""
		cleaned_t = len(self.cleaned)
		h = 0
		for i, word in enumerate(self.unique_words):
			h += 1
			# if h%1000 == 0:
			# 	print h
			for j, word_tmp in enumerate(self.cleaned):
				# If it is the last one then just skip it
				if j == (cleaned_t - 1):
					continue
				if self.unique_words[i] == self.cleaned[j]:
					# Find the index of the next word and increase its counter by 1.
					self.appearances[i][ self.unique_words.index( self.cleaned[j + 1] ) ] += 1
	def normalize(self):
		""" Makes the result of appearances between 0.0 and 1.0 depending on the total for that particular word """
		for i in range(self.t):
			total = sum(self.appearances[i])
			total = total if total > 0.0 else 1.0
			# print total
			for j in range(self.t):
				try:
					self.appearances[i][j] /= total
				except:
					print (self.appearances[i][j])
					print (total)
	def generate_probabilities(self):
		""" 
			Fill array of probabilities according to the normalized values of appearances.
			Each row in probabilities represents a unique word.
			Each cell in each row of probabilities contains an index of a unique word; and the number of 
			times that index appears in the row is proportional to how many times it follows that particular word.
		"""
		for i in range(self.t):
			k = 0
			for j in range(self.t):
				if self.appearances[i][j] != 0.0:
					tmp = int(self.appearances[i][j]*100)
					tmp = tmp if tmp != 100 else 99
					for l in range(tmp):
						self.probabilities[i][k] = j
						k += 1
						k = k if k != 100 else 99
	def obtain_word(self, i):
		"""
			Just obtains a random word by accessing the probabilities list.
			i equals the row = current word.
		"""
		k = int( random.random() * 100 )
		return self.unique_words[ int(self.probabilities[int(i)][int(k)]) ], self.probabilities[int(i)][int(k)]
	def speak(self, n, start = None):
		""" Obtains n words, using start as the initial word """
		if (not start) or (start not in self.unique_words):
			k = int( self.t * random.random() )
			k = k if k != self.t else self.t-1
			start = self.unique_words[k]
		final = []
		current_word = start
		current_index = self.unique_words.index(start)
		for i in range(n):
			final.append(current_word)
			current_word = ''
			i = 0
			while current_word == '':
				i += 1
				new_word, new_index = self.obtain_word(current_index)
				current_word = new_word
				# if current_word in final:
				# 	current_word = ''
				# if current_word == 'system':
				# 	current_word = ''
				if current_word != '':
					current_index = new_index
				if i % 20 == 0:
					i = 1
					current_index = new_index
		return ' '.join(final)
	def speakZarathustra(self, n, start = None):
		""" Alias for speak() """	
		return self.speak(n, start)

containers = { type_of_text : Analysis(type_of_text) for type_of_text in types_of_text }

def ipsum(type_of_text, paragraphs, words = 40):
	"""
		type_of_text <String> Must be a key of types_of_text defined at the top of the file.
		paragraphs <Integer> Numbet of total paragraphs.
		words <Integer> Number of words per paragraph.
	"""
	final = []
	container = containers[type_of_text]
	container.load()
	for i in range(paragraphs):
		final.append('\t'+container.speak(words).capitalize()+'.'	)
	return '\n\n'.join(final)

if __name__=="__main__":
	print (ipsum('scifi', 2, 60))
