var availableTags = [
    "مسابقه والیبال ایران و آمریکا",
    "مسابقه فوتبال ایران و ترکیه",
    "کشتی پیشکسوتان جهان"
];
$("#autocomplete").autocomplete({
    source: availableTags,
    delay: 400,
    minLength: 2
});