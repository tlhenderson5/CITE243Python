FavShow = input("What's your favorite show? ").strip().title()
FavArc = input("What's your favorite story arc? ").strip().title()
if FavShow == 'One Piece' and FavArc == 'Enies Lobby':
 print('You have good taste in anime and I like your favorite story arc choice!')
elif FavShow == 'One Piece':
 print('Good taste in anime! But you should rewatch Enies Lobby!')
else:
 print('You should watch One Piece and check out the Enies Lobby arc!')