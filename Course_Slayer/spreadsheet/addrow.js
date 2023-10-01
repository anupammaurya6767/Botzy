const { GoogleSpreadsheet } = require('google-spreadsheet');
const fs = require('fs');

const doc = new GoogleSpreadsheet("YOUR_SPREADSHEET_ID");
var file = 'credentials.json'; //add your credentials.json for google sheets
const CREDENTIALS = JSON.parse(fs.readFileSync(file));
module.exports = async (rows) => {

    await doc.useServiceAccountAuth({
        client_email: CREDENTIALS.client_email,
        private_key: CREDENTIALS.private_key
    });

    await doc.loadInfo();

    let sheet = doc.sheetsByIndex[0];

    for (let index = 0; index < rows.length; index++) {
        const row = rows[index];
        await sheet.addRow(row);
    }
   };