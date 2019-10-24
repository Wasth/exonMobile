let clickAC = 0, clickCOI = 0, clickGS = 0, clickSAA = 0, FIO = '', company = '';
$('#PrimaryEMail').on('blur', function () {
    let email = $(this).val();
    let text = 'Please enter a valid email address.';
    if (email.length > 0
        && (email.match(/.+?\@.+/g) || []).length !== 1) {
        console.log('invalid');
        document.getElementById('invalidPrimaryEmail').hidden = false;
        document.getElementById('invalidPrimaryEmail').innerHTML = text;
        $('#PrimaryEMail').css("border-left", "3px solid #d5000a");
        $('#PrimaryEMailLabel').css("color", "#d5000a");
    } else {
        $('#PrimaryEMail').css("border-left", "1px solid #d1d3d4");
        $('#PrimaryEMailLabel').css("color", "#6d6e71");
        document.getElementById('invalidPrimaryEmail').hidden = true;
        console.log('valid');
    }
});

function selectAnnualCashflow() {
    let chceck = $('#AnnualCashflow :selected');
    if (clickAC === 0) {
        clickAC++;
        console.log(chceck.val());
    } else {
        clickAC--;
        document.getElementById('AnnualCashflowSpan').innerHTML = chceck[0].innerText;
    }
}

function selectServiceAreaAvailable() {
    let chceck = $('#ServiceAreaAvailable :selected');
    if (clickSAA === 0) {
        clickSAA++;
        console.log(chceck.val());
    } else {
        clickSAA--;
        document.getElementById('ServiceAreaAvailableSpan').innerHTML = chceck[0].innerText;
    }
}

function selectGoodsServicesList() {
    let chceck = $('#GoodsServicesList :selected');
    if (clickGS === 0) {
        clickGS++;
        console.log(chceck.val());
    } else {
        clickGS--;
        document.getElementById('GoodsServicesListSpan').innerHTML = chceck[0].innerText;
    }
}

function selectCountryOfIncorporation() {
    let chceck = $('#CountryOfIncorporation :selected');
    if (clickCOI === 0) {
        clickCOI++;
        console.log(chceck.val());
    } else {
        clickCOI--;
        document.getElementById('CountryOfIncorporationSpan').innerHTML = chceck[0].innerText;
    }
}

$("#PrimaryContactPhone").keypress(function (event) {
    event = event || window.event;
    if (event.charCode && event.charCode != 0 && event.charCode != 46 && (event.charCode < 48 || event.charCode > 57))
        return false;
});
$("#SecondaryContactPhone").keypress(function (event) {
    event = event || window.event;
    if (event.charCode && event.charCode != 0 && event.charCode != 46 && (event.charCode < 48 || event.charCode > 57))
        return false;
});

$(function () {
    $('#PrimaryContactPhone').mask('+9(999)999-99-99');
    $('#SecondaryContactPhone').mask('+9(999)999-99-99');
});

$('#PrimaryContactName').on('keyup', function (e) {
    FIO = $(this).val();
    console.log($(this).val())
});

$('#CompanyName').on('keyup', function (e) {
    company = $(this).val();
    console.log($(this).val())
});

$('#policy').on('click', function () {
    modal = $('.modal-cover, .modal, .modal-content, #modal');
    $('#textPolicy').html(`
            Проставляя отметку в настоящей ячейке, я <u>` + FIO + `</u>, действуя от имени и в
            интересах <u>` + company + `</u>, заявляю, что я должным
            образом уполномочен(а) раскрывать предоставленную информацию, включая персональные
            данные , и подтверждаю, что даю компании "Эксон Нефтегаз Лимитед" (далее – ЭНЛ)
            согласие на обработку персональных данных и что, мною получено согласие от
            упомянутых в анкете лиц, отличных от меня, на предоставление ЭНЛ персональных данных
            для обработки в целях, связанных с возможными деловыми отношениями с компанией ЭНЛ в
            рамках проекта "Сахалин-1".`);
    modal.fadeIn();
});

$('.modal').click(function () {
    modal = $('.modal-cover, .modal, .modal-content, #modal');
    $('#wrapper').on('click', function (event) {
        var select = $('.content');
        if ($(event.target).closest(select).length)
            return;
        modal.fadeOut();
        $('#wrapper').unbind('click');
    });
});

