#!/usr/bin/python

import sys,time

text = ''' 
I let it fall, my heart,
And as it fell you rose to claim it
It was dark and I was over
Until you kissed my lips and you saved me

My hands, they're strong
But my knees were far too weak,
To stand in your arms
Without falling to your feet

But there's a side to you
That I never knew, never knew.
All the things you'd say
They were never true, never true,
And the games you play
You would always win, always win.

[Chorus:]
But I set fire to the rain,
Watched it pour as I touched your face,
Well, it burned while I cried
'Cause I heard it screaming out your name, your name!

When I lay with you
I could stay there
Close my eyes
Feel you here forever
You and me together
Nothing gets better

'Cause there's a side to you
That I never knew, never knew,
All the things you'd say,
They were never true, never true,
And the games you'd play
You would always win, always win.

[Chorus:]
But I set fire to the rain,
Watched it pour as I touched your face,
Well, it burned while I cried
'Cause I heard it screaming out your name, your name!

I set fire to the rain
And I threw us into the flames
When it fell, something died
'Cause I knew that that was the last time, the last time!

Sometimes I wake up by the door,
That heart you caught must be waiting for you
Even now when we're already over
I can't help myself from looking for you.

[Chorus:]
I set fire to the rain,
Watched it pour as I touched your face,
Well, it burned while I cried
'Cause I heard it screaming out your name, your name

I set fire to the rain,
And I threw us into the flames
When it fell, something died
'Cause I knew that that was the last time, the last time, ohhhh!

Oh noooo
Let it burn, oh
Let it burn
Let it burn
'''

def printone(l):
 for i in l:
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(.05)
printone(text)
