let datetime = "";

module.exports = () => {
    var currentdate = new Date();
    datetime = "Requested on: " + currentdate.getDay() + "/" + currentdate.getMonth() 
    + "/" + currentdate.getFullYear() + " @ " 
    + currentdate.getHours() + ":" 
    + currentdate.getMinutes() + ":" + currentdate.getSeconds();

    return datetime;
}