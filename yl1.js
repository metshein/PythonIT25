const data = [
  ["11/1/2024","4/5/2024","Narva","Tartu",141.6,"sedan","Puce",1241,"1/19/1994"],
  ["14/3/2024","17/5/2024","Haapsalu","Tartu",278.4,"sport","Pink",9219,"12/10/1981"],
  ["10/2/2024","29/6/2024","Kohtla-Järve","Haapsalu",271.4,"sport","Fuscia",359,"7/31/1998"],
  ["11/2/2024","10/7/2024","Võru","Rakvere",176.2,"sport","Khaki",6929,"10/30/1984"],
  ["25/1/2024","5/5/2024","Võru","Rakvere",23.2,"SUV","Mauv",4028,"10/8/1994"],
  ["13/1/2024","6/9/2024","Haapsalu","Tallinn",77.6,"sport","Puce",6517,"11/3/1997"],
  ["28/1/2024","1/6/2024","Haapsalu","Kuressaare",37.7,"sedan","Purple",8295,"9/23/1976"],
  ["9/1/2024","20/10/2024","Viljandi","Pärnu",208.1,"sedan","Green",7853,"4/15/1978"],
  ["19/2/2024","23/6/2024","Narva","Haapsalu",313.7,"SUV","Violet",1697,"5/6/1979"],
  ["18/2/2024","21/10/2024","Kohtla-Järve","Kohtla-Järve",153.2,"sedan","Blue",5532,"1/31/1990"],
  ["27/2/2024","17/5/2024","Tartu","Viljandi",345.3,"SUV","Blue",8416,"8/23/1990"],
  ["3/1/2024","29/5/2024","Kohtla-Järve","Viljandi",80.8,"SUV","Indigo",1754,"7/23/1994"],
  ["14/1/2024","2/8/2024","Kuressaare","Rakvere",289.6,"sedan","Green",635,"5/13/1976"],
  ["5/2/2024","6/8/2024","Võru","Kuressaare",179.2,"sport","Blue",2449,"4/8/1997"],
  ["24/1/2024","1/6/2024","Tallinn","Rakvere",165.7,"SUV","Red",122,"5/23/1981"],
  ["3/3/2024","8/5/2024","Kuressaare","Viljandi",138.2,"sport","Aquamarine",8729,"11/19/1999"],
  ["17/3/2024","8/8/2024","Kuressaare","Võru",105.0,"sedan","Violet",402,"4/6/1982"],
  ["7/3/2024","23/9/2024","Tallinn","Viljandi",34.3,"SUV","Orange",4259,"3/12/1976"],
  ["5/2/2024","5/10/2024","Viljandi","Võru",171.3,"SUV","Maroon",471,"8/16/1993"],
  ["17/2/2024","29/6/2024","Tartu","Rakvere",197.8,"sedan","Yellow",6236,"7/7/1975"],
  ["29/3/2024","13/5/2024","Tartu","Kuressaare",263.1,"SUV","Crimson",4716,"1/20/1976"],
  ["20/2/2024","18/7/2024","Kohtla-Järve","Kohtla-Järve",183.7,"sedan","Blue",2002,"11/17/1992"],
  ["1/2/2024","23/5/2024","Kuressaare","Kohtla-Järve",170.6,"sport","Goldenrod",9973,"11/4/1998"],
  ["12/3/2024","10/8/2024","Tallinn","Võru",370.8,"sedan","Maroon",4256,"6/19/1982"]
];

let types = []

//  console.log(data[0]);
 for (let i = 0; i < data.length; i++) {
    //  console.log(data[i][5]);
    types.push(data[i][5])
}
 var unique = types.filter((value, index, array) => array.indexOf(value) === index);
 console.log(unique); 
