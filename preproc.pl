#!/usr/bin/perl

$remove_punct = 1;

while(<>){
    next if /isbn/;
    next if /copyright/;
    next if /@/;
    next if /http/;

    next if /-(LCB|RCB|LRB|RRB|LSB|RSB)-/;
    next if /\.jpe?g/;
    next if /_BOOK_TITLE_/;
    next if /CHAPTER/;

    # happens in the movies database !??
    s/^\d+\s//g;

    s/`/'/g;
    s/''/'/g;
    s/\.\.+/./g; # ellipsis

    # deperiod
    s/\bp \. m \./pm/g;
    s/\ba \. m \./am/g;
    s/\bi \. e \./that is/g;
    s/\bmon \./Monday/ig;
    s/\btue \./Tuesday/ig;
    s/\bwed \./Wednesday/ig;
    s/\bthu \./Thursday/ig;
    s/\bfri \./Friday/ig;
    s/\bsat \./Saturday/ig;
    # s/\bsun \./Sunday/g # ambiguous
    s/\bJan \./January/ig;
    s/\bFeb \./February/ig;
    s/\bMar \./March/ig;
    s/\bApr \./April/ig;
    s/\bJun \./June/ig;
    s/\bJul \./July/ig;
    s/\bAug \./August/ig;
    s/\bSep \./September/ig;
    s/\bOct \./October/ig;
    s/\bMr\s?\./Mr/g;
    s/\bMs\s?\./Ms/g;
    s/\bMrs\s?\./Mrs/g;
    s/\bDoc\s?\./doctor/gi;
    s/\bDr\s?\./doctor/gi;

    # dequote
    s/ain 't/is not/ig;
    s/can 't/can not/ig;
    s/'ll /will /g;
    s/n 't /not /g;
    s/'re /are /g;
    s/'d /had /g;
    s/'ve /have /g;
    s/'m /am /g;
    s/he 's /he is /g;
    s/she 's /she is /g;

    s/ain't/is not/ig;
    s/can't/can not/ig;
    s/won't/can not/ig;
    s/n't /not /ig;
    s/he's /he is /ig;
    s/she's /she is/ig;


    #tr/A-Z/a-z/;
    s/0/ zero /g;
    s/1/ one /g;
    s/2/ two /g;
    s/3/ three /g;
    s/4/ four /g;
    s/5/ five /g;
    s/6/ six /g;
    s/7/ seven /g;
    s/8/ eight /g;
    s/9/ nine /g;

    tr/A-Z/a-z/;

    if($remove_punct){
        s/, /COMMA /g;
        s/ '(\s*)/ QUOTE\1/g;
        s/; /SEMICOLON /g;
        s/\.(\s*)/PERIOD\1/g;
        s/\?(\s*)/QUESTIONMARK\1/g;
        s/!(\s*)/EXCLMARK\1/g;
        s/\s*--\s*/ EMDASH /g;
        s/\s:\s/ COLON /g;
    }
    print
}
