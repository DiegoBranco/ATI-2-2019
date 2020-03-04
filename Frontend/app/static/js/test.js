  const reloj = document.getElementById('tiempo');
        let min = reloj.innerHTML[0] + reloj.innerHTML[1];
        let seg = reloj.innerHTML[3] + reloj.innerHTML[4];

        function showTime(mins){
            return (seg < 10 && seg !== "00") ? mins + ':' + '0' + seg : mins + ':' + seg;
        }
        function timercount(mins){
            if (seg > 0){
                seg = seg - 1;
            }else {
                mins = mins - 1;
                seg = 59;
            }
            return mins
        }

        function iterador(){
            if(min > 0 || seg > 0){
                min = timercount(min);
                reloj.innerHTML = showTime(min)
            }else {
                clearInterval(iden);
                reloj.innerHTML = showTime(min);
                alert("Se te acabó el tiempo, más suerte a la próxima.")
            }
        }
        let iden = setInterval(function(){
            iterador()},1000);