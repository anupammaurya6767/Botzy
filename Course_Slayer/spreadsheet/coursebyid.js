const { GoogleSpreadsheet } = require('google-spreadsheet');
const fs = require('fs');

const doc = new GoogleSpreadsheet("YOUR_SPREADSHEET_ID");
var file = 'credentials.json'; //add your credentials.json for google sheets
const CREDENTIALS = JSON.parse(fs.readFileSync(file));


module.exports = async (courseid) => {
     let resbyid = '🤖 Your requested course: \n \n';

     // use service account creds
     await doc.useServiceAccountAuth({
         client_email: CREDENTIALS.client_email,
         private_key: CREDENTIALS.private_key
     });
     await doc.loadInfo();

     let sheet2 = doc.sheetsByIndex[0];
     let  rows = await sheet2.getRows();
     let maxrow = rows.length
   if(courseid<=maxrow)
   {
     for (let index = 0; index < rows.length; index++) {
       const row = rows[index];
      
        if (row.Course_id === courseid) {
          resbyid += row.Course_id;
          resbyid += '      ';
          resbyid += row.Course_link;
          resbyid += '\n \n';
          resbyid += "Enjoy!"
        
       }

   };
  }else{
      resbyid = "🫠 Id to shi daal na bro! (check  Course_id again)"

  }

  return resbyid;
   };