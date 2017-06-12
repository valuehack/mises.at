var dialog = document.querySelector('#btcdialog');
var dialog2 = document.querySelector('#bankdialog');
var show = document.querySelector('#show');
var show2 = document.querySelector('#show2');

show.addEventListener('click', function() {
  dialog.showModal();
  console.log('dialog opened');
});

show2.addEventListener('click', function() {
  dialog2.showModal();
  console.log('dialog opened');
});

dialog.addEventListener('close', function() {
  console.log('dialog closed');
});

dialog.addEventListener('cancel', function() {
  console.log('dialog canceled');
});

document.querySelector('#close').onclick = function() {
  dialog.close();
};

document.querySelector('#close2').onclick = function() {
  dialog2.close();
};

// (function() {
//     $('form > input').keyup(function() {
//
//         var empty = false;
//         $('form > input').each(function() {
//             if ($(this).val() == '') {
//                 empty = true;
//             }
//         });
//
//         if (empty) {
//             $('#show2').attr('disabled', 'disabled');
//         } else {
//             $('#show2').removeAttr('disabled');
//         }
//     });
// })()
