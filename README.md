# telegram_recommendations

### Goals

This script lists all channels associated with a Telegram account and collects all associated channel recommendations. It only takes into account the top10 recommendations. A future version will make it possible to obtain the remaining recommendations by systematically adhering to the channels. The results are presented in a json file that only takes positive results into account. 

Very interesting if you have a set of channels on the same theme, you can quickly expand the network. Useful for operational monitoring, for example. Remember, you can't subscribe to more than 500 or 1000 (premium) channels with a single account.



### Instructions 

- get the at api_id and hash_id at https://core.telegram.org/api/obtaining_api_id
- put them in the script
- install the library Telethon (pip install telethon)
- launch the script and connect to your account (will not work if MFA is activated)

### Links

https://telegram.org/blog/similar-channels/

https://tl.telethon.dev/methods/channels/get_channel_recommendations.html
