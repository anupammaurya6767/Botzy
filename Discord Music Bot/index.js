const Discord = require('discord.js');
const { MusicBot } = require('discord.js-musicbot-addon');

const client = new Discord.Client();
const token = 'YOUR_BOT_TOKEN'; // Replace with your actual bot token

// Create a new instance of the MusicBot class
const musicBot = new MusicBot({
  botPrefix: '-', // Prefix for bot commands
  youtubeKey: 'YOUR_YOUTUBE_API_KEY', // Replace with your YouTube API key
  botToken: token, // Bot token
  ownerID: 'YOUR_DISCORD_USER_ID', // Your Discord user ID
  musicPresence: false, // Enable/disable music status presence
  clearPresence: true, // Enable/disable clearing bot's presence on inactive
  helpCmd: 'help', // Command to display help
  enableQueueStat: true, // Enable queue status message
  ownerOverMember: true, // Owner can use bot regardless of DJ role
  inlineEmbeds: false, // Enable/disable inline embeds
  musicPlayerInvite: false, // Enable/disable music player invite link
  ownerCmd: 'owner', // Command to display owner-only commands
  enableLive: false, // Enable/disable live notifications
  disableLoop: false, // Enable/disable loop command
  messageHelp: true, // Enable/disable sending help message on invalid commands
});

client.once('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.login(token);
