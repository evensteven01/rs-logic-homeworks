from pytest_mock.plugin import MockerFixture

from src.Logic.variables import *

def _print_call_args(register):
    for call in register.call_args_list:
            print(f"Call: {call}")
            for tup in call:
                print(f"> {tup}")
                for arg in tup:
                    print(f"  > {arg}")

def test_example(mocker: MockerFixture):
    # Arrange
    expected_arg = 1
    register = mocker.patch("src.Logic.variables._cregister")

    # Act
    example()

    # Assert
    register.assert_called_with(expected_arg)
    
def test_create_vars(mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.variables._cregister")
    
    # Act
    create_vars()

    # Assert
    call = register.call_args_list[0]
    assert isinstance(call[0][0], int)
    assert isinstance(call[0][1], str)

def test_create_list(mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.variables._cregister")
    
    # Act
    create_list()

    # Assert
    call = register.call_args_list[0]
    arg1 = call[0][0]
    assert isinstance(arg1, list)
    assert len(arg1) == 3
    assert isinstance(arg1[0], int)

def test_modify_list(mocker: MockerFixture):
        # Arrange
    register = mocker.patch("src.Logic.variables._cregister")
     
    # Act
    modify_list()

    # Assert
    call1 = register.call_args_list[0]
    call2 = register.call_args_list[1]
    arg1_1 = call1[0][0]
    arg1_2 = call2[0][0]
    assert isinstance(arg1_1, list)
    assert isinstance(arg1_2, list)
    assert len(arg1_1) == 3
    assert len(arg1_2) == 3
    for i, v in enumerate(arg1_1):
        assert isinstance(v, int)
        assert arg1_2[i] == v+1
    
def test_add_item_to_list(mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.variables._cregister")
    
    # Act
    add_item_to_list()

    # Assert
    call1 = register.call_args_list[0]
    call2 = register.call_args_list[1]
    arg1_1 = call1[0][0]
    arg1_2 = call2[0][0]
    assert isinstance(arg1_1, list)
    assert isinstance(arg1_2, list)
    assert len(arg1_1) == 2
    assert len(arg1_2) == 3
    for val in arg1_1:
        assert isinstance(val, str)
    


def test_create_str_dict(mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.variables._cregister")
    
    # Act
    create_str_dict()

    # Assert
    call1 = register.call_args_list[0]
    call2 = register.call_args_list[1]
    arg1_1 = call1[0][0]
    arg1_2 = call2[0][0]
    assert isinstance(arg1_1, dict)
    assert isinstance(arg1_2, dict)
    assert len(arg1_1) == 2
    assert len(arg1_2) == 3
    for key, val in arg1_2.items():
        assert isinstance(key, str)
        assert isinstance(val, str)

def test_create_int_dict(mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.variables._cregister")
    
    # Act
    create_int_dict()

    # Assert
    call1 = register.call_args_list[0]
    call2 = register.call_args_list[1]
    arg1_1 = call1[0][0]
    arg1_2 = call2[0][0]
    assert isinstance(arg1_1, dict)
    assert isinstance(arg1_2, dict)
    assert len(arg1_1) == 2
    assert len(arg1_2) == 3
    for key, val in arg1_1.items():
        if isinstance(key, int):
            assert isinstance(val, int)
        else:
            assert False
    for key, val in arg1_2.items():
        if isinstance(key, int):
            assert isinstance(val, int)
        else:
            assert False

def test_create_mixed_dict(mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.variables._cregister")

    # Act
    create_mixed_dict()

    # Assert
    call1 = register.call_args_list[0]
    call2 = register.call_args_list[1]
    arg1_1 = call1[0][0]
    arg1_2 = call2[0][0]
    assert isinstance(arg1_1, dict)
    assert isinstance(arg1_2, dict)
    assert len(arg1_1) == 2
    assert len(arg1_2) == 3
    for key, val in arg1_1.items():
        if isinstance(key, int):
            assert isinstance(val, str)
        elif isinstance(key, str):
            assert isinstance(val, int)
        else:
            assert False
    for key, val in arg1_2.items():
        if isinstance(key, int):
            assert isinstance(val, str)
        elif isinstance(key, str):
            assert isinstance(val, int)
        elif isinstance(key, float):
            assert isinstance(val, list)
        else:
            assert False


def test_update_dict(mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.variables._cregister")
    
    # Act
    update_dict()

    # Assert
    call1 = register.call_args_list[0]
    call2 = register.call_args_list[1]
    arg1_1 = call1[0][0]
    arg1_2 = call2[0][0]
    assert isinstance(arg1_1, dict)
    assert isinstance(arg1_2, dict)
    assert len(arg1_1) == 2
    assert len(arg1_2) == 2
    
    num_diff = 0
    for key, val in arg1_1.items():
        if val != arg1_2[key]:
            num_diff+=1

    assert num_diff == 1


def test_remove_item_dict(mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.variables._cregister")
    
    # Act
    remove_item_dict()

    # Assert
    call1 = register.call_args_list[0]
    call2 = register.call_args_list[1]
    arg1_1 = call1[0][0]
    arg1_2 = call2[0][0]
    assert isinstance(arg1_1, dict)
    assert isinstance(arg1_2, dict)
    assert len(arg1_1) == len(arg1_2)+1

def test_build_dict(mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.variables._cregister")
    
    # Act
    build_dict()

    # Assert
    call1 = register.call_args_list[0]
    call2 = register.call_args_list[1]
    arg1_1 = call1[0][0]
    arg2_1 = call1[0][1]
    arg1_2 = call2[0][0]
    assert isinstance(arg1_1, list)
    assert isinstance(arg2_1, list)
    assert len(arg1_1) == len(arg2_1)

    assert isinstance(arg1_2, dict)

    for index, key in enumerate(arg1_1):
        assert isinstance(key, str)
        val = arg1_2[key]
        assert isinstance(val, int)
        assert arg2_1[index] == val
