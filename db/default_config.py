#!/usr/bin/env python
# -*- coding: utf-8 -*-

USER_LIST = [{
    'username': 'test',
    'email': 'test@test.com',
    'password': '123',
    'first_name': 'Test',
    'last_name': 'Bug',
    'active': True
}]

BLOG_LIST = [
    {
        "title": "Computer science",
        "content": u"Computer science is the study of the theory, experimentation, and engineering that form the basis for the design and use of computers. It is the scientific and practical approach to computation and its applications and the systematic study of the feasibility, structure, expression, and mechanization of the methodical procedures (or algorithms) that underlie the acquisition, representation, processing, storage, communication of, and access to information. An alternate, more succinct definition of computer science is the study of automating algorithmic processes that scale. A computer scientist specializes in the theory of computation and the design of computational systems. \n\n Its fields can be divided into a variety of theoretical and practical disciplines. Some fields, such as computational complexity theory (which explores the fundamental properties of computational and intractable problems), are highly abstract, while fields such as computer graphics emphasize real-world visual applications. Other fields still focus on challenges in implementing computation. For example, programming language theory considers various approaches to the description of computation, while the study of computer programming itself investigates various aspects of the use of programming language and complex systems. Human–computer interaction considers the challenges in making computers and computations useful, usable, and universally accessible to humans.",
        "user_id": 1,
        "header": "is the study of theory"
    },
    {
        "title": "Video Game",
        "content": u"A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device such as a TV screen or computer monitor. The word video in video game traditionally referred to a raster display device, but as of the 2000s, it implies any type of display device that can produce two- or three-dimensional images. Some theorists categorize video games as an art form, but this designation is controversial. \n\n The electronic systems used to play video games are known as platforms; examples of these are personal computers and video game consoles. These platforms range from large mainframe computers to small handheld computing devices. Specialized video games such as arcade games, in which the video game components are housed in a large, coin-operated chassis, while common in the 1980s in video arcades, have gradually declined in use due to the widespread availability of affordable home video game consoles (e.g., PlayStation 4 and Xbox One) and video games on desktop and laptop computers and smartphones. \n\n The input device used for games, the game controller, varies across platforms. Common controllers include gamepads, joysticks, mouses, keyboards, the touchscreens of mobile devices and buttons. Players typically view the game on a video screen or television and there are often game sounds from loudspeakers. Some games in the 2000s include haptic, vibration-creating effects, force feedback peripherals and virtual reality headsets. In the 2010s, the video game industry is of increasing commercial importance, with growth driven particularly by the emerging Asian markets and mobile games, which are played on smartphones. As of 2015, video games generated sales of USD 74 billion annually worldwide, and were the third-largest segment in the U.S. entertainment market, behind broadcast and cable TV.",
        "user_id": 1
    },
    {
        "title": "Giant panda",
        "content": u"The giant panda (Ailuropoda melanoleuca, literally \"black and white cat-foot\"; Chinese: 大熊猫; pinyin: dà xióng māo, literally \"big bear cat\"),[3] also known as panda bear or simply panda, is a bear[4] native to south central China.[1] It is easily recognized by the large, distinctive black patches around its eyes, over the ears, and across its round body. The name \"giant panda\" is sometimes used to distinguish it from the unrelated red panda. Though it belongs to the order Carnivora, the giant panda's diet is over 99% bamboo.[5] Giant pandas in the wild will occasionally eat other grasses, wild tubers, or even meat in the form of birds, rodents or carrion. In captivity, they may receive honey, eggs, fish, yams, shrub leaves, oranges, or bananas along with specially prepared food.\nThe giant panda lives in a few mountain ranges in central China, mainly in Sichuan province, but also in neighbouring Shaanxi and Gansu.[8] As a result of farming, deforestation, and other development, the giant panda has been driven out of the lowland areas where it once lived.\nThe giant panda is a conservation reliant vulnerable species.[9][10] A 2007 report showed 239 pandas living in captivity inside China and another 27 outside the country.[11] As of December 2014, 49 giant pandas lived in captivity outside China, living in 18 zoos in 13 different countries.[12] Wild population estimates vary; one estimate shows that there are about 1,590 individuals living in the wild,[11] while a 2006 study via DNA analysis estimated that this figure could be as high as 2,000 to 3,000.[13] Some reports also show that the number of giant pandas in the wild is on the rise.[14] In March 2015, Mongabay stated that the wild giant panda population had increased by 268, or 16.8%, to 1,864 individuals.[15] In 2016, the IUCN reclassified the species from endangered to vulnerable[10] (it did not believe there was enough certainty yet to do so in 2008[16]).\n",
        "user_id": 1
    },
    {
        "title": "Smartphone",
        "content": u"A smartphone is a mobile phone (also known as cell phones) with an advanced mobile operating system which combines features of a personal computer operating system with other features useful for mobile or handheld use.[1][2][3] Smartphones, which are usually pocket-sized, typically combine the features of a mobile phone, such as the abilities to place and receive voice calls and create and receive text messages, with those of other popular digital mobile devices like personal digital assistants (PDAs), such as an event calendar, media player, video games, GPS navigation, digital camera and digital video camera. Most smartphones can access the Internet and can run a variety of third-party software components (\"apps\"). They typically have a color display with a graphical user interface that covers 70% or more of the front surface. The display is often a touchscreen, which enables the user to use a virtual keyboard to type words and numbers and press onscreen icons to activate \"app\" features. \n In 1999, the Japanese firm NTT DoCoMo released the first smartphones to achieve mass adoption within a country.[4] Smartphones became widespread in the late 2000s. Most of those produced from 2012 onward have high-speed mobile broadband 4G LTE, motion sensors, and mobile payment features. In the third quarter of 2012, one billion smartphones were in use worldwide.[5] Global smartphone sales surpassed the sales figures for regular cell phones in early 2013.[6] As of 2013, 65% of mobile consumers in the United States owned smartphones.[7] By January 2016, smartphones held over 79% of the U.S. mobile market",
        "user_id": 1,
        "header": "The future"
    },
    {
        "title": u"只是中文",
        "content": u"测试能不\n\n能显示中文",
        "user_id": 1,
        "header": u"另个 注明"
    },
    {
        "title": u"a",
        "content": u"a",
        "user_id": 1,
        "header": u"a"
    },
    {
        "title": u"b",
        "content": u"b",
        "user_id": 1,
        "header": u"c"
    },
    {
        "title": u"d",
        "content": u"d",
        "user_id": 1,
        "header": u"d"
    },
    {
        "title": u"e",
        "content": u"e",
        "user_id": 1,
        "header": u"e"
    },
    {
        "title": u"f",
        "content": u"f",
        "user_id": 1,
        "header": u"f"
    },
    {
        "title": u"2",
        "content": u"2",
        "user_id": 1,
        "header": u"2"
    },
    {
        "title": u"3",
        "content": u"3",
        "user_id": 1,
        "header": u"3"
    },
    {
        "title": u"4",
        "content": u"4",
        "user_id": 1,
        "header": u"4"
    },
    {
        "title": u"5",
        "content": u"5",
        "user_id": 1,
        "header": u"5"
    },
    {
        "title": u"6",
        "content": u"6",
        "user_id": 1,
        "header": u"6"
    },
]
