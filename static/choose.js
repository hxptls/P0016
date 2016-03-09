/**
 * Created by wan on 3/9/16.
 */
'use strict';
$(function() {
    let chosenCount = 0;
    for (let x = 0; x < 19; x++) {
        for (let y = 0; y < 19; y++) {
            const div_id = '#classroom-seat-' + x + '-' + y;
            $(div_id).click(function () {
                if (chosenCount >= 4) {
                    alert('妈的智障');
                    return;
                }
                alert('正在选座……');
                const seat_type = chosenCount == 0 ? 'b' : 's';
                $.get('/choose', {
                    's': seat_type, 'x': x, 'y': y, 'n': 'hex'
                }, function(req) {
                    if (req === 'ok') {
                        const the_div = div_id +
                            (seat_type === 'b' ? '>.best' : '>.soso');
                        $(the_div).html('hex');
                        alert('选座成功');
                        chosenCount++;
                    }
                })
            })
        }
    }
});
