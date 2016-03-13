/**
 * Created by wan on 3/13/16.
 */
$('#classroom-container').ready(function() {
    var maxRight = 0;
    $('.classroom-seat').each(function(n, ele) {
        maxRight = Math.max(maxRight, ele.offsetLeft + ele.offsetWidth);
    });
    $('.classroom-row').each(function(n, ele) {
        ele.style.width = '' + (maxRight + 10) + 'px';
    });
});