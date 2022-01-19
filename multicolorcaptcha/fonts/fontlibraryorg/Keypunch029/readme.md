# Keypunch029

Stewart C. Russell - scruss.com
2017-03

A fairly accurate rendition of the 5×7 dot matrix font printed at the
top of punched cards by the IBM Type 29 Card Punch (1965). The 029 (as
it is sometimes known) generated a bitmap font from an engraved metal
plate pressing on a matrix of pins. A picture of this plate from a
field engineering manual was used to re-create the pin matrices, and
thus an outline font.

## Coverage

Upper case ASCII only and a few special characters (€, £, ⌑ and ¬).

## Design Size

12 pt

## Variants

Regular, Italic, Bold and Bold-Italic. (The last three aren't
historically accurate.)


## Source

Source to all fonts is included in FontForge format. The JSON bitmaps
and Python source are also included.

## Licence

Copyright © 2017, Stewart C. Russell (scruss.com),
with Reserved Font Name Keypunch029.

This Font Software is licensed under the SIL Open Font Licence, Version 1.1.
This licence is included, and is also available with a FAQ at:
http://scripts.sil.org/OFL

[I do not agree with SIL's missionary work in any way, and the use of
this licence is in no way an endorsement of SIL.]

## Version

1.0

## Historical Accuracy

The 029 could have many different code plates, but the one used here
contained the characters:

    <=>¬|_-,;:!?/.'"()@¢$*&#%+0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

The character glyphs have been sized such that if printed at 12
points, the 029's character pitch of 0.087" is accurately
reproduced. No attempt to research the pin matrix pitch or pin
diameter has been made: the spacing was eyeballed from a couple of
punched cards in my collection.

The earlier IBM Type 26 Card Punch ("026") included a glyph for a
square lozenge (Unicode U+2311, ⌑). The 029 code plate did not include
this character, but I added it here for completeness.

The character set was extended to include:

* all of ASCII, with lower case characters repeating the upper case
  glyphs;

* sterling currency symbol; and
  
* euro currency symbol.

While there may have been official IBM renditions of some of these
additional glyphs (with the exception of euro) no attempt has been
made to research the original shapes.

This font set is intended to help with the visually accurate
reproduction of 1960s-era punched cards, mostly coinciding with my
interest in the FORTRAN programming language. No attempt has been made
to use historical BCD/EBCDIC encodings in these fonts. We have Unicode
now.

The 029 card punch could not produce any bold or italic font variants,
but FontForge can, so I did.

## Things I learned in making these fonts

1. The 029 card punch printer could be damaged if you tried to print
   binary cards, as there was no way to disengage the code plate from
   the punch mechanism.
   
2. FontForge *really* hates to have paths in a glyph just
   touching. Either keep them more than one unit apart, or overlap
   them and merge the overlapping paths.
   
3. EBCDIC is **weird**.

## Sources

* Norbert Landsteiner's
  amazing
  [Punched Card Typography Explained](http://www.masswerk.at/misc/card-punch-typography/ "Punched Card Typography Explained") page describes
  how the code plate system worked, and has JavaScript animations
  showing how characters were decoded (entirely mechanically) from the plate.

*
  [IBM029-Field-Eng-Maint-Man-r.pdf](http://www.ed-thelen.org/comp-hist/IBM029-Field-Eng-Maint-Man-r.pdf "IBM029-Field-Eng-Maint-Man-r.pdf") -
  see page 59 for the code plate image. The site's owner is part of
  the [IBM 1401 Demo Lab and Restoration Project](http://ibm-1401.info/index.html "IBM 1401 Demo Lab and Restoration Project").
  
*
  [Douglas W. Jones's punched card index](http://homepage.divms.uiowa.edu/~jones/cards/index.html "Douglas W. Jones's punched card index") is
  *all* about punched cards.
