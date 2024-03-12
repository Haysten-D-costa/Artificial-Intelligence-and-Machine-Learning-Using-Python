checkChar = function(ch) {
  if (ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u' || ch=='A' || ch=='E' || ch=='I' || ch=='O' || ch=='U') {
    print(paste("Character is a vowel !"));
  } else {
    print(paste("Character is a consonant !"));
  }
}
ch = readline("Enter a character : ");
ch = as.character(ch);
checkChar(ch)
