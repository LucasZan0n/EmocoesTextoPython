# Importando NLTK para PLN (Processamento de Linguagem Natural)
import nltk

nltk.download('punkt')  # Tokenização de textos
nltk.download('movie_reviews')  # Reviews de filmes

# Importar modulo LeXmo do pacote LeXmo
from LeXmo import LeXmo

# Texto que será classificado as emoções:
t = """When I look into your eyes
I can see a love restrained
But darlin' when I hold you
Don't you know I feel the same?
Nothin' lasts forever
And we both know hearts can change
And it's hard to hold a candle
In the cold November rain
We've been through this such a long long time
Just tryin' to kill the pain, ooh yeah
Love is always coming, love is always going
No one's really sure who's lettin' go today
Walking away
If we could take the time to lay it on the line
I could rest my head just knowin' that you were mine
All mine
So if you want to love me then darlin' don't refrain
Or I'll just end up walkin' in the cold November rain
Do you need some time on your own?
Do you need some time all alone?
Ooh, everybody needs some time on their own
Ooh, don't you know you need some time all alone
I know it's hard to keep an open heart
When even friends seem out to harm you
But if you could heal a broken heart
Wouldn't time be out to charm you?
Oh, oh, oh
Sometimes I need some time on my own
Sometimes I need some time all alone
Ooh, everybody needs some time on their own
Ooh, don't you know you need some time all alone
And when your fears subside
And shadows still remain, oh yeah
I know that you can love me when there's no one left to blame
So never mind the darkness, we still can find a way
'Cause nothin' lasts forever, even cold November rain
Don't ya think that you need somebody?
Don't ya think that you need someone?
Everybody needs somebody
You're not the only one
You're not the only one
Don't ya think that you need somebody?
Don't ya think that you need someone?
Everybody needs somebody
You're not the only one
You're not the only one
Don't ya think that you need somebody?
Don't ya think that you need someone?
Everybody needs somebody
You're not the only one
You're not the only one
Don't ya think that you need somebody?
Don't ya think that you need someone?
Everybody needs somebody
"""

emo = LeXmo.LeXmo(t)
emo.pop('text', None)
print(emo)
