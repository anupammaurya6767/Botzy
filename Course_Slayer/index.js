const TelegramBot = require("node-telegram-bot-api");
const course = require("./spreadsheet/getcourse.js");
const byid = require("./spreadsheet/coursebyid.js");
const request = require("./spreadsheet/addrow.js");
const timeevent = require("./datetime/datetime.js");

// Replace the value below with the Telegram token you receive from @BotFather
const token = "YOUR_BOT_TOKEN";

// Create a bot that uses 'polling' to fetch new updates
const bot = new TelegramBot(token, { polling: true });

console.log("Bot Started");

// Listen for any kind of message. There are different kinds of messages.

bot.onText(/\/list/, async (msg) => {
  const {
    message_id: originalMessageId,
    from: { username },
    chat: { id: chatId },
  } = msg;
  let val = false;
  if (msg.chat.id === -1001264908544) val = true;

  let res =
    "🍥 Here is the list of all Mega Courses Available:\n \n https://docs.google.com/spreadsheets/d/1uL3OvcbgRdIa0dmjkh8VWEnAJQ42aMr5p9paDLKyRIA/edit?usp=sharing \n \n get course_id and use !get command 😌";
  if (val) {
    bot.sendMessage(msg.chat.id, res, {
      reply_to_message_id: originalMessageId,
    });
  } else {
    bot.sendMessage(msg.chat.id, "Group pe use kro bro!");
  }
});

bot.onText(/\/request (.+)/, async (msg, match) => {
  const {
    message_id: originalMessageId,
    from: { username },
    chat: { id: chatId },
  } = msg;
  let val = false;
  if (msg.chat.id === -1001264908544) val = true;
  const resp = match[1];
  let rest =
    "✌️ Your Request has been submitted successfully! \n \n ✔️ Check Status! ==> https:docs.google.com/spreadsheets/d/1dI-8EBXPUeRVi7Xn8fOYs6x2hXlz8M7sDrQZqlM8ZOI/edit?usp=sharing";
  let rows = [
    {
      Request: resp,
      On_Date: timeevent(),
      Status: "Working...",
    },
  ];

  await request(rows);
  if (val) {
    bot.sendMessage(msg.chat.id, rest, {
      reply_to_message_id: originalMessageId,
    });
  } else {
    bot.sendMessage(msg.chat.id, "Group pe use kro bro!");
  }
});

bot.onText(/\/get (.+)/, async (msg, match) => {
  const {
    message_id: originalMessageId,
    from: { username },
    chat: { id: chatId },
  } = msg;
  let val = false;
  if (msg.chat.id === -1001264908544) val = true;
  const resp = match[1];
  let rest = "";
  await byid(resp).then((res) => {
    rest = res;
  });
  if (val) {
    bot.sendMessage(msg.chat.id, rest, {
      reply_to_message_id: originalMessageId,
    });
  } else {
    bot.sendMessage(msg.chat.id, "Group pe use kro bro!");
  }
});
