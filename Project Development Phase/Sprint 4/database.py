var m=global.get('m')
var d=new Date();
var utc=d.getTime()+(d.getTimezoneOffset()*60000);
var offset=5.5;
newDate=new Date(utc+(3600000*offset));
var n=newDate.toISOString()
var date=n.slice(0,10)
var time=n.slice(11,19)
var d1=date+','+time

msg.payload={
    "_id":d1,
    "Name":m.Name,
    "Age":m.Age,
    "Mobile":m.Num,
    "boarding":global.get('b'),
    "destination":global.get('d'),
    "Seat":global.get('s')
}
return msg;
