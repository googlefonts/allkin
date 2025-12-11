## FontSpector report

fontspector version: 1.5.0






## Check results




<details><summary>[14] fonts/ttf/Allkin-Regular.ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Font contains glyphs for whitespace characters? (whitespace_glyphs)</summary>
    <div>








- 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0 [code: missing-whitespace-glyph-0x00A0]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- 🔥 **FAIL** No GF glyphset was found to be supported >80%, so language shaping support couldn't get checked. [code: no-glyphset-supported]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Name table strings must not contain the string 'Reserved Font Name'. (googlefonts/name/rfn)</summary>
    <div>








- 🔥 **FAIL** Name table entry contains "Reserved Font Name":
	"Copyright © 2025 Monotype Imaging Inc., with Reserved Font Name Allkin."

This is bad except in a few specific rare cases. [code: rfn]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Directory name in GFonts repo structure must
    match NameID 1 of the regular. (googlefonts/repo/dirname_matches_nameid_1)</summary>
    <div>








- 🔥 **FAIL** Family name on the name table ('Allkin') does not match directory name in the repo structure ('ttf'). Expected 'allkin'. [code: mismatch]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure font can render its own name. (googlefonts/render_own_name)</summary>
    <div>








- 🔥 **FAIL** .notdef glyphs were found when attempting to render Allkin [code: render-own-name]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check font follows the Google Fonts vertical metric schema (googlefonts/vertical_metrics)</summary>
    <div>








- 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1200 when it should be at least 2400 [code: bad-hhea-range]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>








- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* cold (U+E04F): found 3, expected one of: {21, 2, 15}
* hurt (U+E061): found 25, expected one of: {4, 6, 2}
* attack (U+E073): found 4, expected one of: {2, 1, 11}
* transport_ground (U+E087): found 8, expected one of: {3, 13, 2}
* three_us_china (U+E0A7): found 3, expected one of: {4, 1, 2}
* three_japan (U+E0A8): found 2, expected one of: {9, 3, 1}
* five_japan (U+E0AE): found 4, expected one of: {2, 3, 1}
* converge (U+E0B6): found 2, expected one of: {5, 1, 8} [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? (gpos_kerning_info)</summary>
    <div>








- ⚠️ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure indic fonts have the Indian Rupee Sign glyph. (rupee)</summary>
    <div>








- ⚠️ **WARN** Font is missing the Indian Rupee Sign glyph. Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9. [code: missing-rupee]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following separator glyphs are missing:

* U+2028
* U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? (outline_colinear_vectors)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have colinear vectors:

* ok (U+E010): Line { p0: (389.0, 837.0), p1: (418.0, 585.0) } -> Line { p0: (418.0, 585.0), p1: (431.0, 420.0) }
* payment_japan (U+E02B): Line { p0: (619.0, 437.0), p1: (454.0, 428.0) } -> Line { p0: (454.0, 428.0), p1: (200.0, 422.0) }
* speak (U+E034): Line { p0: (314.0, 918.0), p1: (403.0, 926.0) } -> Line { p0: (403.0, 926.0), p1: (446.0, 930.0) }
* calm (U+E04E): Line { p0: (619.0, 437.0), p1: (454.0, 428.0) } -> Line { p0: (454.0, 428.0), p1: (200.0, 422.0) }
* curious (U+E053): Line { p0: (85.0, 423.0), p1: (98.0, 588.0) } -> Line { p0: (98.0, 588.0), p1: (127.0, 840.0) }
* curious (U+E053): Line { p0: (796.0, 840.0), p1: (825.0, 588.0) } -> Line { p0: (825.0, 588.0), p1: (838.0, 423.0) }
* perfect (U+E08E): Line { p0: (85.0, 413.0), p1: (98.0, 578.0) } -> Line { p0: (98.0, 578.0), p1: (127.0, 830.0) }
* perfect_italy (U+E08F): Line { p0: (705.0, 492.0), p1: (471.0, 588.0) } -> Line { p0: (471.0, 588.0), p1: (320.0, 657.0) }
* clarifying (U+E091): Line { p0: (314.0, 878.0), p1: (403.0, 886.0) } -> Line { p0: (403.0, 886.0), p1: (446.0, 890.0) }
* three_japan (U+E0A8): Line { p0: (205.0, 552.0), p1: (204.0, 586.0) } -> Line { p0: (204.0, 586.0), p1: (204.0, 692.0) }
* container (U+E0B5): Line { p0: (314.0, 910.0), p1: (403.0, 918.0) } -> Line { p0: (403.0, 918.0), p1: (446.0, 922.0) }
* container (U+E0B5): Line { p0: (614.0, 922.0), p1: (657.0, 918.0) } -> Line { p0: (657.0, 918.0), p1: (746.0, 910.0) }
* far (U+E0B8): Line { p0: (85.0, 421.0), p1: (98.0, 586.0) } -> Line { p0: (98.0, 586.0), p1: (127.0, 838.0) }
* far (U+E0B8): Line { p0: (796.0, 838.0), p1: (825.0, 586.0) } -> Line { p0: (825.0, 586.0), p1: (838.0, 421.0) }
* symbol (U+E0C4): Line { p0: (419.0, 640.0), p1: (508.0, 731.0) } -> Line { p0: (508.0, 731.0), p1: (527.0, 750.0) }
* symbol (U+E0C4): Line { p0: (545.0, 560.0), p1: (456.0, 469.0) } -> Line { p0: (456.0, 469.0), p1: (436.0, 450.0) } [code: found-colinear-vectors]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? (outline_jaggy_segments)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have jaggy segments:

* safe (U+E008): Line(Line { p0: (343.0, 824.0), p1: (500.0, 825.0) })/Quad(QuadBez { p0: (500.0, 825.0), p1: (464.0, 832.0), p2: (464.0, 873.0) }) = 11.368477187480158
* safe (U+E008): Line(Line { p0: (652.0, 378.0), p1: (495.0, 377.0) })/Quad(QuadBez { p0: (495.0, 377.0), p1: (531.0, 370.0), p2: (531.0, 329.0) }) = 11.368477187480158
* speak (U+E034): Line(Line { p0: (286.0, 926.0), p1: (239.0, 890.0) })/Line(Line { p0: (239.0, 890.0), p1: (282.0, 936.0) }) = 9.480009209430257
* when (U+E042): Line(Line { p0: (618.0, 573.0), p1: (505.0, 681.0) })/Quad(QuadBez { p0: (505.0, 681.0), p1: (526.0, 651.0), p2: (497.0, 622.0) }) = 11.304043299458481
* heart02_korea (U+E05E): Line(Line { p0: (460.0, 780.0), p1: (350.0, 668.0) })/Quad(QuadBez { p0: (350.0, 668.0), p1: (379.0, 689.0), p2: (409.0, 659.0) }) = 9.606441150587191
* serenity (U+E06B): Quad(QuadBez { p0: (693.5, 563.0), p1: (689.0, 589.0), p2: (670.0, 597.0) })/Line(Line { p0: (670.0, 597.0), p1: (917.0, 544.0) }) = 10.723056410263125
* shyness (U+E06D): Line(Line { p0: (652.0, 599.0), p1: (495.0, 598.0) })/Quad(QuadBez { p0: (495.0, 598.0), p1: (531.0, 591.0), p2: (531.0, 550.0) }) = 11.368477187480158
* shyness (U+E06D): Quad(QuadBez { p0: (879.0, 550.0), p1: (879.0, 591.0), p2: (915.0, 598.0) })/Line(Line { p0: (915.0, 598.0), p1: (758.0, 599.0) }) = 11.368477187480158
* evacuate (U+E07A): Line(Line { p0: (296.0, 708.0), p1: (375.0, 573.0) })/Quad(QuadBez { p0: (375.0, 573.0), p1: (363.0, 608.0), p2: (399.0, 628.0) }) = 11.410894095537635
* clarifying (U+E091): Line(Line { p0: (286.0, 886.0), p1: (239.0, 850.0) })/Line(Line { p0: (239.0, 850.0), p1: (282.0, 896.0) }) = 9.480009209430257
* container (U+E0B5): Line(Line { p0: (286.0, 918.0), p1: (239.0, 882.0) })/Line(Line { p0: (239.0, 882.0), p1: (282.0, 928.0) }) = 9.480009209430257
* container (U+E0B5): Line(Line { p0: (778.0, 928.0), p1: (821.0, 882.0) })/Line(Line { p0: (821.0, 882.0), p1: (774.0, 918.0) }) = 9.480009209430257
* converge (U+E0B6): Quad(QuadBez { p0: (442.0, 752.0), p1: (478.0, 732.0), p2: (466.0, 697.0) })/Line(Line { p0: (466.0, 697.0), p1: (545.0, 832.0) }) = 11.410894095537635
* converge (U+E0B6): Line(Line { p0: (759.0, 832.0), p1: (838.0, 697.0) })/Quad(QuadBez { p0: (838.0, 697.0), p1: (826.0, 732.0), p2: (862.0, 752.0) }) = 11.410894095537635
* more (U+E0BC): Line(Line { p0: (548.0, 801.0), p1: (429.0, 699.0) })/Quad(QuadBez { p0: (429.0, 699.0), p1: (461.0, 717.0), p2: (487.0, 685.0) }) = 11.243541102213227
* picture (U+E0BE): Line(Line { p0: (343.0, 824.0), p1: (500.0, 825.0) })/Quad(QuadBez { p0: (500.0, 825.0), p1: (464.0, 832.0), p2: (464.0, 873.0) }) = 11.368477187480158
* picture (U+E0BE): Line(Line { p0: (652.0, 378.0), p1: (495.0, 377.0) })/Quad(QuadBez { p0: (495.0, 377.0), p1: (531.0, 370.0), p2: (531.0, 329.0) }) = 11.368477187480158 [code: found-jaggy-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? (outline_semi_vertical)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

* safe (U+E008): Line(Line { p0: (343.0, 824.0), p1: (500.0, 825.0) })
* safe (U+E008): Line(Line { p0: (652.0, 378.0), p1: (495.0, 377.0) })
* connection (U+E01A): Line(Line { p0: (218.0, 662.0), p1: (220.0, 914.0) })
* connection (U+E01A): Line(Line { p0: (305.0, 904.0), p1: (303.0, 657.0) })
* connection (U+E01A): Line(Line { p0: (741.0, 657.0), p1: (739.0, 904.0) })
* connection (U+E01A): Line(Line { p0: (824.0, 914.0), p1: (826.0, 662.0) })
* faster (U+E01E): Line(Line { p0: (579.0, 296.0), p1: (444.0, 295.0) })
* speakup (U+E036): Line(Line { p0: (579.0, 296.0), p1: (444.0, 295.0) })
* flourishing (U+E058): Line(Line { p0: (718.0, 684.0), p1: (717.0, 926.0) })
* flourishing (U+E058): Line(Line { p0: (461.0, 926.0), p1: (460.0, 684.0) })
* shyness (U+E06D): Line(Line { p0: (652.0, 599.0), p1: (495.0, 598.0) })
* shyness (U+E06D): Line(Line { p0: (915.0, 598.0), p1: (758.0, 599.0) })
* death_western (U+E078): Line(Line { p0: (461.0, 926.0), p1: (460.0, 684.0) })
* picture (U+E0BE): Line(Line { p0: (343.0, 824.0), p1: (500.0, 825.0) })
* picture (U+E0BE): Line(Line { p0: (652.0, 378.0), p1: (495.0, 377.0) }) [code: found-semi-vertical]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>








- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>


</div>
</details>


<details><summary>[3] fonts/ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Copyright notices match canonical pattern in fonts (googlefonts/font_copyright)</summary>
    <div>








- 🔥 **FAIL** Allkin-Regular.ttf: Name Table entry: Copyright notices should match a pattern similar to:

"Copyright 2020 The Familyname Project Authors (git url)"

But instead we have got:

"copyright © 2025 monotype imaging inc., with reserved font name allkin." [code: bad-notice-format]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. (googlefonts/glyph_coverage)</summary>
    <div>








- 🔥 **FAIL** fonts/ttf/Allkin-Regular.ttf missing required codepoints:

* 0x0021: EXCLAMATION MARK
* 0x0022: QUOTATION MARK
* 0x0023: NUMBER SIGN
* 0x0024: DOLLAR SIGN
* 0x0025: PERCENT SIGN
* 0x0026: AMPERSAND
* 0x0027: APOSTROPHE
* 0x0028: LEFT PARENTHESIS
* 0x0029: RIGHT PARENTHESIS
* 0x002A: ASTERISK
* 0x002B: PLUS SIGN
* 0x002C: COMMA
* 0x002D: HYPHEN-MINUS
* 0x002E: FULL STOP
* 0x002F: SOLIDUS
* 0x0030: DIGIT ZERO
* 0x0031: DIGIT ONE
* 0x0032: DIGIT TWO
* 0x0033: DIGIT THREE
* 0x0034: DIGIT FOUR
* 0x0035: DIGIT FIVE
* 0x0036: DIGIT SIX
* 0x0037: DIGIT SEVEN
* 0x0038: DIGIT EIGHT
* 0x0039: DIGIT NINE
* 0x003A: COLON
* 0x003B: SEMICOLON
* 0x003C: LESS-THAN SIGN
* 0x003D: EQUALS SIGN
* 0x003E: GREATER-THAN SIGN
* 0x003F: QUESTION MARK
* 0x0040: COMMERCIAL AT
* 0x0041: LATIN CAPITAL LETTER A
* 0x0042: LATIN CAPITAL LETTER B
* 0x0043: LATIN CAPITAL LETTER C
* 0x0044: LATIN CAPITAL LETTER D
* 0x0045: LATIN CAPITAL LETTER E
* 0x0046: LATIN CAPITAL LETTER F
* 0x0047: LATIN CAPITAL LETTER G
* 0x0048: LATIN CAPITAL LETTER H
* 0x0049: LATIN CAPITAL LETTER I
* 0x004A: LATIN CAPITAL LETTER J
* 0x004B: LATIN CAPITAL LETTER K
* 0x004C: LATIN CAPITAL LETTER L
* 0x004D: LATIN CAPITAL LETTER M
* 0x004E: LATIN CAPITAL LETTER N
* 0x004F: LATIN CAPITAL LETTER O
* 0x0050: LATIN CAPITAL LETTER P
* 0x0051: LATIN CAPITAL LETTER Q
* 0x0052: LATIN CAPITAL LETTER R
* 0x0053: LATIN CAPITAL LETTER S
* 0x0054: LATIN CAPITAL LETTER T
* 0x0055: LATIN CAPITAL LETTER U
* 0x0056: LATIN CAPITAL LETTER V
* 0x0057: LATIN CAPITAL LETTER W
* 0x0058: LATIN CAPITAL LETTER X
* 0x0059: LATIN CAPITAL LETTER Y
* 0x005A: LATIN CAPITAL LETTER Z
* 0x005B: LEFT SQUARE BRACKET
* 0x005C: REVERSE SOLIDUS
* 0x005D: RIGHT SQUARE BRACKET
* 0x005E: CIRCUMFLEX ACCENT
* 0x005F: LOW LINE
* 0x0060: GRAVE ACCENT
* 0x0061: LATIN SMALL LETTER A
* 0x0062: LATIN SMALL LETTER B
* 0x0063: LATIN SMALL LETTER C
* 0x0064: LATIN SMALL LETTER D
* 0x0065: LATIN SMALL LETTER E
* 0x0066: LATIN SMALL LETTER F
* 0x0067: LATIN SMALL LETTER G
* 0x0068: LATIN SMALL LETTER H
* 0x0069: LATIN SMALL LETTER I
* 0x006A: LATIN SMALL LETTER J
* 0x006B: LATIN SMALL LETTER K
* 0x006C: LATIN SMALL LETTER L
* 0x006D: LATIN SMALL LETTER M
* 0x006E: LATIN SMALL LETTER N
* 0x006F: LATIN SMALL LETTER O
* 0x0070: LATIN SMALL LETTER P
* 0x0071: LATIN SMALL LETTER Q
* 0x0072: LATIN SMALL LETTER R
* 0x0073: LATIN SMALL LETTER S
* 0x0074: LATIN SMALL LETTER T
* 0x0075: LATIN SMALL LETTER U
* 0x0076: LATIN SMALL LETTER V
* 0x0077: LATIN SMALL LETTER W
* 0x0078: LATIN SMALL LETTER X
* 0x0079: LATIN SMALL LETTER Y
* 0x007A: LATIN SMALL LETTER Z
* 0x007B: LEFT CURLY BRACKET
* 0x007C: VERTICAL LINE
* 0x007D: RIGHT CURLY BRACKET
* 0x007E: TILDE
* 0x00A0: NO-BREAK SPACE
* 0x00A1: INVERTED EXCLAMATION MARK
* 0x00A2: CENT SIGN
* 0x00A3: POUND SIGN
* 0x00A5: YEN SIGN
* 0x00A7: SECTION SIGN
* 0x00A8: DIAERESIS
* 0x00A9: COPYRIGHT SIGN
* 0x00AA: FEMININE ORDINAL INDICATOR
* 0x00AB: LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
* 0x00AE: REGISTERED SIGN
* 0x00AF: MACRON
* 0x00B0: DEGREE SIGN
* 0x00B4: ACUTE ACCENT
* 0x00B6: PILCROW SIGN
* 0x00B7: MIDDLE DOT
* 0x00B8: CEDILLA
* 0x00BA: MASCULINE ORDINAL INDICATOR
* 0x00BB: RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
* 0x00BF: INVERTED QUESTION MARK
* 0x00C0: LATIN CAPITAL LETTER A WITH GRAVE
* 0x00C1: LATIN CAPITAL LETTER A WITH ACUTE
* 0x00C2: LATIN CAPITAL LETTER A WITH CIRCUMFLEX
* 0x00C3: LATIN CAPITAL LETTER A WITH TILDE
* 0x00C4: LATIN CAPITAL LETTER A WITH DIAERESIS
* 0x00C5: LATIN CAPITAL LETTER A WITH RING ABOVE
* 0x00C6: LATIN CAPITAL LETTER AE
* 0x00C7: LATIN CAPITAL LETTER C WITH CEDILLA
* 0x00C8: LATIN CAPITAL LETTER E WITH GRAVE
* 0x00C9: LATIN CAPITAL LETTER E WITH ACUTE
* 0x00CA: LATIN CAPITAL LETTER E WITH CIRCUMFLEX
* 0x00CB: LATIN CAPITAL LETTER E WITH DIAERESIS
* 0x00CC: LATIN CAPITAL LETTER I WITH GRAVE
* 0x00CD: LATIN CAPITAL LETTER I WITH ACUTE
* 0x00CE: LATIN CAPITAL LETTER I WITH CIRCUMFLEX
* 0x00CF: LATIN CAPITAL LETTER I WITH DIAERESIS
* 0x00D0: LATIN CAPITAL LETTER ETH
* 0x00D1: LATIN CAPITAL LETTER N WITH TILDE
* 0x00D2: LATIN CAPITAL LETTER O WITH GRAVE
* 0x00D3: LATIN CAPITAL LETTER O WITH ACUTE
* 0x00D4: LATIN CAPITAL LETTER O WITH CIRCUMFLEX
* 0x00D5: LATIN CAPITAL LETTER O WITH TILDE
* 0x00D6: LATIN CAPITAL LETTER O WITH DIAERESIS
* 0x00D7: MULTIPLICATION SIGN
* 0x00D8: LATIN CAPITAL LETTER O WITH STROKE
* 0x00D9: LATIN CAPITAL LETTER U WITH GRAVE
* 0x00DA: LATIN CAPITAL LETTER U WITH ACUTE
* 0x00DB: LATIN CAPITAL LETTER U WITH CIRCUMFLEX
* 0x00DC: LATIN CAPITAL LETTER U WITH DIAERESIS
* 0x00DD: LATIN CAPITAL LETTER Y WITH ACUTE
* 0x00DE: LATIN CAPITAL LETTER THORN
* 0x00DF: LATIN SMALL LETTER SHARP S
* 0x00E0: LATIN SMALL LETTER A WITH GRAVE
* 0x00E1: LATIN SMALL LETTER A WITH ACUTE
* 0x00E2: LATIN SMALL LETTER A WITH CIRCUMFLEX
* 0x00E3: LATIN SMALL LETTER A WITH TILDE
* 0x00E4: LATIN SMALL LETTER A WITH DIAERESIS
* 0x00E5: LATIN SMALL LETTER A WITH RING ABOVE
* 0x00E6: LATIN SMALL LETTER AE
* 0x00E7: LATIN SMALL LETTER C WITH CEDILLA
* 0x00E8: LATIN SMALL LETTER E WITH GRAVE
* 0x00E9: LATIN SMALL LETTER E WITH ACUTE
* 0x00EA: LATIN SMALL LETTER E WITH CIRCUMFLEX
* 0x00EB: LATIN SMALL LETTER E WITH DIAERESIS
* 0x00EC: LATIN SMALL LETTER I WITH GRAVE
* 0x00ED: LATIN SMALL LETTER I WITH ACUTE
* 0x00EE: LATIN SMALL LETTER I WITH CIRCUMFLEX
* 0x00EF: LATIN SMALL LETTER I WITH DIAERESIS
* 0x00F0: LATIN SMALL LETTER ETH
* 0x00F1: LATIN SMALL LETTER N WITH TILDE
* 0x00F2: LATIN SMALL LETTER O WITH GRAVE
* 0x00F3: LATIN SMALL LETTER O WITH ACUTE
* 0x00F4: LATIN SMALL LETTER O WITH CIRCUMFLEX
* 0x00F5: LATIN SMALL LETTER O WITH TILDE
* 0x00F6: LATIN SMALL LETTER O WITH DIAERESIS
* 0x00F7: DIVISION SIGN
* 0x00F8: LATIN SMALL LETTER O WITH STROKE
* 0x00F9: LATIN SMALL LETTER U WITH GRAVE
* 0x00FA: LATIN SMALL LETTER U WITH ACUTE
* 0x00FB: LATIN SMALL LETTER U WITH CIRCUMFLEX
* 0x00FC: LATIN SMALL LETTER U WITH DIAERESIS
* 0x00FD: LATIN SMALL LETTER Y WITH ACUTE
* 0x00FE: LATIN SMALL LETTER THORN
* 0x00FF: LATIN SMALL LETTER Y WITH DIAERESIS
* 0x0100: LATIN CAPITAL LETTER A WITH MACRON
* 0x0101: LATIN SMALL LETTER A WITH MACRON
* 0x0102: LATIN CAPITAL LETTER A WITH BREVE
* 0x0103: LATIN SMALL LETTER A WITH BREVE
* 0x0104: LATIN CAPITAL LETTER A WITH OGONEK
* 0x0105: LATIN SMALL LETTER A WITH OGONEK
* 0x0106: LATIN CAPITAL LETTER C WITH ACUTE
* 0x0107: LATIN SMALL LETTER C WITH ACUTE
* 0x010A: LATIN CAPITAL LETTER C WITH DOT ABOVE
* 0x010B: LATIN SMALL LETTER C WITH DOT ABOVE
* 0x010C: LATIN CAPITAL LETTER C WITH CARON
* 0x010D: LATIN SMALL LETTER C WITH CARON
* 0x010E: LATIN CAPITAL LETTER D WITH CARON
* 0x010F: LATIN SMALL LETTER D WITH CARON
* 0x0110: LATIN CAPITAL LETTER D WITH STROKE
* 0x0111: LATIN SMALL LETTER D WITH STROKE
* 0x0112: LATIN CAPITAL LETTER E WITH MACRON
* 0x0113: LATIN SMALL LETTER E WITH MACRON
* 0x0116: LATIN CAPITAL LETTER E WITH DOT ABOVE
* 0x0117: LATIN SMALL LETTER E WITH DOT ABOVE
* 0x0118: LATIN CAPITAL LETTER E WITH OGONEK
* 0x0119: LATIN SMALL LETTER E WITH OGONEK
* 0x011A: LATIN CAPITAL LETTER E WITH CARON
* 0x011B: LATIN SMALL LETTER E WITH CARON
* 0x011E: LATIN CAPITAL LETTER G WITH BREVE
* 0x011F: LATIN SMALL LETTER G WITH BREVE
* 0x0120: LATIN CAPITAL LETTER G WITH DOT ABOVE
* 0x0121: LATIN SMALL LETTER G WITH DOT ABOVE
* 0x0122: LATIN CAPITAL LETTER G WITH CEDILLA
* 0x0123: LATIN SMALL LETTER G WITH CEDILLA
* 0x0126: LATIN CAPITAL LETTER H WITH STROKE
* 0x0127: LATIN SMALL LETTER H WITH STROKE
* 0x012A: LATIN CAPITAL LETTER I WITH MACRON
* 0x012B: LATIN SMALL LETTER I WITH MACRON
* 0x012E: LATIN CAPITAL LETTER I WITH OGONEK
* 0x012F: LATIN SMALL LETTER I WITH OGONEK
* 0x0130: LATIN CAPITAL LETTER I WITH DOT ABOVE
* 0x0131: LATIN SMALL LETTER DOTLESS I
* 0x0136: LATIN CAPITAL LETTER K WITH CEDILLA
* 0x0137: LATIN SMALL LETTER K WITH CEDILLA
* 0x0139: LATIN CAPITAL LETTER L WITH ACUTE
* 0x013A: LATIN SMALL LETTER L WITH ACUTE
* 0x013B: LATIN CAPITAL LETTER L WITH CEDILLA
* 0x013C: LATIN SMALL LETTER L WITH CEDILLA
* 0x013D: LATIN CAPITAL LETTER L WITH CARON
* 0x013E: LATIN SMALL LETTER L WITH CARON
* 0x0141: LATIN CAPITAL LETTER L WITH STROKE
* 0x0142: LATIN SMALL LETTER L WITH STROKE
* 0x0143: LATIN CAPITAL LETTER N WITH ACUTE
* 0x0144: LATIN SMALL LETTER N WITH ACUTE
* 0x0145: LATIN CAPITAL LETTER N WITH CEDILLA
* 0x0146: LATIN SMALL LETTER N WITH CEDILLA
* 0x0147: LATIN CAPITAL LETTER N WITH CARON
* 0x0148: LATIN SMALL LETTER N WITH CARON
* 0x0150: LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
* 0x0151: LATIN SMALL LETTER O WITH DOUBLE ACUTE
* 0x0152: LATIN CAPITAL LIGATURE OE
* 0x0153: LATIN SMALL LIGATURE OE
* 0x0154: LATIN CAPITAL LETTER R WITH ACUTE
* 0x0155: LATIN SMALL LETTER R WITH ACUTE
* 0x0158: LATIN CAPITAL LETTER R WITH CARON
* 0x0159: LATIN SMALL LETTER R WITH CARON
* 0x015A: LATIN CAPITAL LETTER S WITH ACUTE
* 0x015B: LATIN SMALL LETTER S WITH ACUTE
* 0x015E: LATIN CAPITAL LETTER S WITH CEDILLA
* 0x015F: LATIN SMALL LETTER S WITH CEDILLA
* 0x0160: LATIN CAPITAL LETTER S WITH CARON
* 0x0161: LATIN SMALL LETTER S WITH CARON
* 0x0164: LATIN CAPITAL LETTER T WITH CARON
* 0x0165: LATIN SMALL LETTER T WITH CARON
* 0x016A: LATIN CAPITAL LETTER U WITH MACRON
* 0x016B: LATIN SMALL LETTER U WITH MACRON
* 0x016E: LATIN CAPITAL LETTER U WITH RING ABOVE
* 0x016F: LATIN SMALL LETTER U WITH RING ABOVE
* 0x0170: LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
* 0x0171: LATIN SMALL LETTER U WITH DOUBLE ACUTE
* 0x0172: LATIN CAPITAL LETTER U WITH OGONEK
* 0x0173: LATIN SMALL LETTER U WITH OGONEK
* 0x0174: LATIN CAPITAL LETTER W WITH CIRCUMFLEX
* 0x0175: LATIN SMALL LETTER W WITH CIRCUMFLEX
* 0x0176: LATIN CAPITAL LETTER Y WITH CIRCUMFLEX
* 0x0177: LATIN SMALL LETTER Y WITH CIRCUMFLEX
* 0x0178: LATIN CAPITAL LETTER Y WITH DIAERESIS
* 0x0179: LATIN CAPITAL LETTER Z WITH ACUTE
* 0x017A: LATIN SMALL LETTER Z WITH ACUTE
* 0x017B: LATIN CAPITAL LETTER Z WITH DOT ABOVE
* 0x017C: LATIN SMALL LETTER Z WITH DOT ABOVE
* 0x017D: LATIN CAPITAL LETTER Z WITH CARON
* 0x017E: LATIN SMALL LETTER Z WITH CARON
* 0x0218: LATIN CAPITAL LETTER S WITH COMMA BELOW
* 0x0219: LATIN SMALL LETTER S WITH COMMA BELOW
* 0x021A: LATIN CAPITAL LETTER T WITH COMMA BELOW
* 0x021B: LATIN SMALL LETTER T WITH COMMA BELOW
* 0x0237: LATIN SMALL LETTER DOTLESS J
* 0x02C6: MODIFIER LETTER CIRCUMFLEX ACCENT
* 0x02C7: CARON
* 0x02D8: BREVE
* 0x02D9: DOT ABOVE
* 0x02DA: RING ABOVE
* 0x02DB: OGONEK
* 0x02DC: SMALL TILDE
* 0x02DD: DOUBLE ACUTE ACCENT
* 0x0300: COMBINING GRAVE ACCENT
* 0x0301: COMBINING ACUTE ACCENT
* 0x0302: COMBINING CIRCUMFLEX ACCENT
* 0x0303: COMBINING TILDE
* 0x0304: COMBINING MACRON
* 0x0306: COMBINING BREVE
* 0x0307: COMBINING DOT ABOVE
* 0x0308: COMBINING DIAERESIS
* 0x030A: COMBINING RING ABOVE
* 0x030B: COMBINING DOUBLE ACUTE ACCENT
* 0x030C: COMBINING CARON
* 0x0326: COMBINING COMMA BELOW
* 0x0327: COMBINING CEDILLA
* 0x0328: COMBINING OGONEK
* 0x1E80: LATIN CAPITAL LETTER W WITH GRAVE
* 0x1E81: LATIN SMALL LETTER W WITH GRAVE
* 0x1E82: LATIN CAPITAL LETTER W WITH ACUTE
* 0x1E83: LATIN SMALL LETTER W WITH ACUTE
* 0x1E84: LATIN CAPITAL LETTER W WITH DIAERESIS
* 0x1E85: LATIN SMALL LETTER W WITH DIAERESIS
* 0x1E9E: LATIN CAPITAL LETTER SHARP S
* 0x1EF2: LATIN CAPITAL LETTER Y WITH GRAVE
* 0x1EF3: LATIN SMALL LETTER Y WITH GRAVE
* 0x2013: EN DASH
* 0x2014: EM DASH
* 0x2018: LEFT SINGLE QUOTATION MARK
* 0x2019: RIGHT SINGLE QUOTATION MARK
* 0x201A: SINGLE LOW-9 QUOTATION MARK
* 0x201C: LEFT DOUBLE QUOTATION MARK
* 0x201D: RIGHT DOUBLE QUOTATION MARK
* 0x201E: DOUBLE LOW-9 QUOTATION MARK
* 0x2022: BULLET
* 0x2026: HORIZONTAL ELLIPSIS
* 0x2039: SINGLE LEFT-POINTING ANGLE QUOTATION MARK
* 0x203A: SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
* 0x20AC: EURO SIGN
* 0x2122: TRADE MARK SIGN
* 0x2212: MINUS SIGN [code: missing-codepoints]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>








- ⚠️ **WARN** fonts/ttf/Allkin-Regular.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+0000 : try adding one of: cherokee, mro, deseret, sunuwar, bhaiksuki, tagalog, toto, todhri, symbols, caucasian-albanian, old-south-arabian, indic-siyaq-numbers, marchen, thai, devanagari, meroitic-hieroglyphs, samaritan, lepcha, vithkuqi, meroitic-cursive, gurmukhi, newa, tai-viet, modi, tangsa, telugu, old-hungarian, garay, anatolian-hieroglyphs, ogham, old-turkic, makasar, tai-le, tulu-tigalari, mongolian, egyptian-hieroglyphs, old-permic, tamil-supplement, saurashtra, znamenny, sinhala, sundanese, kaithi, runic, syriac, bamum, ethiopic, gurung-khema, avestan, old-sogdian, ottoman-siyaq-numbers, armenian, siddham, khojki, osmanya, lao, signwriting, imperial-aramaic, mayan-numerals, tifinagh, hanifi-rohingya, khitan-small-script, buhid, chinese-hongkong, syloti-nagri, tamil, pau-cin-hau, glagolitic, manichaean, ugaritic, zanabazar-square, gunjala-gondi, meroitic, bassa-vah, elymaic, batak, nabataean, nandinagari, osage, nag-mundari, takri, mandaic, cham, latin-ext, nyiakeng-puachue-hmong, meetei-mayek, kharoshthi, sogdian, warang-citi, oriya, yi, korean, ol-onal, tai-tham, kawi, kannada, adlam, myanmar, inscriptional-parthian, ahom, palmyrene, sharada, tirhuta, cypro-minoan, malayalam, vietnamese, cyrillic, miao, tibetan, inscriptional-pahlavi, javanese, canadian-aboriginal, symbols2, carian, grantha, ol-chiki, chinese-traditional, vai, coptic, bengali, elbasan, japanese, yezidi, gujarati, cuneiform, psalter-pahlavi, linear-a, kirat-rai, braille, arabic, greek-ext, gothic, masaram-gondi, music, lisu, new-tai-lue, latin, rejang, dives-akuru, buginese, nko, old-persian, hatran, pahawh-hmong, mahajani, medefaidrin, duployan, phoenician, sora-sompeng, dogra, chinese-simplified, cyrillic-ext, soyombo, chorasmian, old-italic, cypriot, hebrew, lydian, mende-kikakui, kayah-li, khudawadi, old-north-arabian, georgian, old-uyghur, shavian, thaana, phags-pa, tagbanwa, limbu, brahmi, multani, wancho, greek, balinese, math, kana-extended, khmer, nushu, linear-b, chakma, hanunoo, lycian, tangut
* U+000D : try adding one of: pau-cin-hau, tagalog, duployan, toto, inscriptional-parthian, meetei-mayek, miao, tifinagh, yi, grantha, bassa-vah, chakma, oriya, armenian, brahmi, glagolitic, old-south-arabian, old-sogdian, old-north-arabian, malayalam, mandaic, runic, tai-viet, myanmar, tamil, balinese, caucasian-albanian, egyptian-hieroglyphs, mayan-numerals, latin, old-hungarian, japanese, psalter-pahlavi, devanagari, soyombo, syriac, tangsa, tibetan, wancho, gujarati, limbu, greek, nag-mundari, chinese-hongkong, manichaean, sinhala, tirhuta, vai, linear-b, sundanese, cyrillic-ext, georgian, indic-siyaq-numbers, osage, korean, ahom, carian, chorasmian, nyiakeng-puachue-hmong, buhid, mende-kikakui, khitan-small-script, inscriptional-pahlavi, thai, bhaiksuki, marchen, yezidi, samaritan, hatran, sunuwar, new-tai-lue, old-italic, old-uyghur, siddham, cypro-minoan, chinese-simplified, chinese-traditional, javanese, khmer, tulu-tigalari, lydian, latin-ext, cuneiform, shavian, kannada, newa, lepcha, warang-citi, dogra, palmyrene, cham, elbasan, pahawh-hmong, cherokee, mongolian, vietnamese, meroitic-cursive, thaana, kharoshthi, multani, symbols, tamil-supplement, canadian-aboriginal, bengali, math, zanabazar-square, signwriting, tai-le, lao, nandinagari, takri, ottoman-siyaq-numbers, arabic, gothic, symbols2, telugu, vithkuqi, old-turkic, phoenician, ogham, meroitic-hieroglyphs, ol-onal, kana-extended, rejang, old-permic, dives-akuru, greek-ext, meroitic, coptic, kaithi, music, avestan, khudawadi, gurmukhi, mro, todhri, deseret, khojki, medefaidrin, modi, sogdian, kirat-rai, makasar, nabataean, tangut, adlam, cyrillic, batak, kayah-li, lycian, nushu, gurung-khema, old-persian, buginese, osmanya, hanunoo, lisu, sora-sompeng, tagbanwa, tai-tham, imperial-aramaic, hanifi-rohingya, bamum, gunjala-gondi, masaram-gondi, ol-chiki, kawi, braille, mahajani, sharada, hebrew, nko, elymaic, phags-pa, ethiopic, cypriot, garay, linear-a, syloti-nagri, saurashtra, ugaritic, znamenny, anatolian-hieroglyphs
* U+0020 SPACE: try adding one of: yi, sinhala, hanifi-rohingya, gujarati, hatran, kana-extended, phoenician, symbols2, miao, hanunoo, imperial-aramaic, runic, braille, chorasmian, nabataean, ottoman-siyaq-numbers, warang-citi, deseret, khmer, ol-chiki, meetei-mayek, vai, medefaidrin, meroitic-cursive, old-permic, tamil, tangsa, toto, old-north-arabian, vithkuqi, tulu-tigalari, linear-a, mongolian, sora-sompeng, balinese, malayalam, lycian, elbasan, tifinagh, syriac, kannada, devanagari, gurung-khema, japanese, mende-kikakui, modi, nko, cyrillic, kharoshthi, music, kirat-rai, old-sogdian, adlam, cyrillic-ext, signwriting, soyombo, avestan, myanmar, ogham, buhid, nag-mundari, inscriptional-pahlavi, ugaritic, javanese, chinese-traditional, greek-ext, mro, old-hungarian, coptic, symbols, canadian-aboriginal, georgian, tibetan, inscriptional-parthian, ol-onal, lepcha, psalter-pahlavi, ahom, duployan, mahajani, batak, sharada, khitan-small-script, sundanese, mandaic, old-uyghur, bamum, chakma, armenian, cypro-minoan, kaithi, caucasian-albanian, khojki, shavian, arabic, kayah-li, cherokee, math, phags-pa, tamil-supplement, old-italic, marchen, carian, telugu, old-south-arabian, old-turkic, pau-cin-hau, multani, vietnamese, tai-le, tai-tham, kawi, grantha, egyptian-hieroglyphs, linear-b, ethiopic, cuneiform, mayan-numerals, meroitic, pahawh-hmong, osage, siddham, znamenny, manichaean, tangut, tirhuta, chinese-simplified, palmyrene, limbu, thaana, old-persian, bhaiksuki, chinese-hongkong, cham, khudawadi, masaram-gondi, korean, indic-siyaq-numbers, greek, new-tai-lue, oriya, rejang, todhri, gunjala-gondi, yezidi, gurmukhi, newa, takri, thai, latin-ext, meroitic-hieroglyphs, tagalog, hebrew, bassa-vah, syloti-nagri, dogra, nyiakeng-puachue-hmong, anatolian-hieroglyphs, cypriot, brahmi, makasar, zanabazar-square, bengali, elymaic, garay, saurashtra, sogdian, buginese, glagolitic, dives-akuru, lao, lisu, osmanya, lydian, samaritan, gothic, sunuwar, latin, nandinagari, tagbanwa, tai-viet, nushu, wancho

Or you can add the above codepoints to one of the subsets supported by the font:  [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>






### Summary

| 🔥 FAIL | ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|---|
| 8 | 9 | 6 | 84 | 78 | 
| 4% | 5% | 3% | 46% | 42% | 



